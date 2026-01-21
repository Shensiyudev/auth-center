
from pydantic import BaseModel
from schemas.user import User


class AuthInput(BaseModel):
    token: str


class AuthOutput(BaseModel):
    user: User | None
    auth: bool
