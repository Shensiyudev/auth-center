from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import COOKIE_KEY, COOKIE_DOMAIN
from app.config.database import get_db
from app.crud.user import get_user_by_phone
from app.schemas.token import JWTPayload
from app.schemas.user import PhoneLogin
from app.utils import PasswordManager, Token, APIResponse

router = APIRouter()


@router.post("/login")
async def login(pl: PhoneLogin, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_phone(db, pl.phone)

    if not user:
        return APIResponse.bad400(msg="用户不存在")
    if not PasswordManager.verify(pl.password, user.password):
        return APIResponse.bad400(msg="密码错误")

    payload = JWTPayload(user_id=user.id)

    token = await Token.get(payload)
    if token is None:
        token = await Token.create(payload, cache=True)

    resp = APIResponse.success200({'user_id': user.id})
    resp.set_cookie(key=COOKIE_KEY, value=token, domain=COOKIE_DOMAIN)
    return resp


@router.get("/logout")
async def logout(request: Request):
    resp = APIResponse.success200({})

    token = request.cookies.get(COOKIE_KEY)
    if not token:
        return resp

    payload = await Token.decode(token)
    if payload:
        await Token.delete(payload)

    resp.delete_cookie(key=COOKIE_KEY, domain=COOKIE_DOMAIN)
    return resp
