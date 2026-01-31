from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config import HEADER_KEY, API_KEY
from config.database import get_db
from crud.user import get_user_by_id
from schemas import AuthInput, AuthOutput
from utils import Token, APIResponse

router = APIRouter()


@router.post("/varify")
async def varify(request: Request, auth: AuthInput, db: AsyncSession = Depends(get_db)):
    backend_key = request.headers.get(HEADER_KEY)
    if backend_key != API_KEY:
        return APIResponse.bad400(msg="api-key required")

    # 验证token
    token = auth.token
    payload = await Token.decode(token)

    if not payload:
        return APIResponse.success200(AuthOutput(), code=1)

    # 验证缓存
    if not await Token.exists(payload):
        return APIResponse.success200(AuthOutput(), code=2)

    # 验证用户
    user = await get_user_by_id(db, payload.user_id)
    if not user:
        return APIResponse.success200(AuthOutput(), code=3)

    # 刷新 token
    await Token.cache(payload, token)

    return APIResponse.success200(AuthOutput(user=user.values(), auth=True))
