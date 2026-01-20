
import jwt

from app.config.redis import rc
from app.config.log import logger
from app.schemas import JWTPayload

from app.config import TOKEN_EXPIRE


class Token:
    SECRET_KEY = "b77247689c65ba2e03bd611f73555954"
    ALGORITHM = "HS256"

    @classmethod
    async def create(cls, payload: JWTPayload, *, cache: bool = False) -> str:
        data = payload.model_dump()
        token = jwt.encode(data, cls.SECRET_KEY, algorithm=cls.ALGORITHM)
        if cache:
            await cls.cache(payload, token)
        return token

    @classmethod
    async def cache(cls, payload: JWTPayload, token: str):
        rc.set(payload.user_id, token, TOKEN_EXPIRE)

    @classmethod
    async def decode(cls, token: str) -> JWTPayload | None:
        try:
            data = jwt.decode(token, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])
            return JWTPayload(**data)
        except jwt.exceptions.DecodeError:
            logger.info('Token解析失败')
            return None
        except jwt.exceptions.ExpiredSignatureError:
            logger.info('Token已过期')
            return None

    @classmethod
    async def get(cls, payload: JWTPayload) -> str | None:
        return rc.get(payload.user_id)

    @classmethod
    async def exists(cls, payload: JWTPayload) -> bool:
        return rc.exists(payload.user_id)

    @classmethod
    async def delete(cls, payload: JWTPayload):
        rc.delete(payload.user_id)
