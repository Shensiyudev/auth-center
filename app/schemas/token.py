from datetime import datetime

from pydantic import BaseModel, Field

from app.config import TOKEN_EXPIRE


class JWTPayload(BaseModel):
    user_id: int
    exp: int = Field(default_factory=lambda: int(datetime.utcnow().timestamp()) + TOKEN_EXPIRE + 1)
