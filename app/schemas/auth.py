
from pydantic import BaseModel
from app.schemas.user import User


class AuthInput(BaseModel):
    token: str


class AuthOutput(BaseModel):
    user: User | None
    auth: bool
