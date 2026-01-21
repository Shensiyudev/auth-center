
from pydantic import BaseModel, Field
from schemas.user import User


class AuthInput(BaseModel):
    token: str


class AuthOutput(BaseModel):
    user: User | None = Field(default=None)
    auth: bool = Field(default=False)
