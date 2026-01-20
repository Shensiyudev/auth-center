from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import HEADER_KEY, API_KEY
from app.config.database import get_db
from app.crud.user import get_user_by_id
from app.schemas import AuthInput, AuthOutput
from app.utils import Token, APIResponse

router = APIRouter()


@router.post("/varify")
async def varify(request: Request, auth: AuthInput, db: AsyncSession = Depends(get_db)):
    backend_key = request.headers.get(HEADER_KEY)
    if backend_key != API_KEY:
        return APIResponse.bad400(msg="无效密钥")

    # 验证token
    token = auth.token
    payload = await Token.decode(token)

    if not payload:
        return APIResponse.success200(AuthOutput(user=None, auth=False), code=1)

    # 验证缓存
    if not await Token.exists(payload):
        return APIResponse.success200(AuthOutput(user=None, auth=False), code=2)

    # 验证用户
    user = await get_user_by_id(db, payload.user_id)
    if not user:
        return APIResponse.success200(AuthOutput(user=None, auth=False), code=3)

    return APIResponse.success200(AuthOutput(user=user.values(), auth=True))
