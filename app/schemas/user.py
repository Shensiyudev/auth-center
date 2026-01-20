from datetime import datetime

from pydantic import BaseModel, Field


class PhoneLogin(BaseModel):
    phone: str = Field(max_length=11, min_length=11)
    password: str = Field(max_length=32, min_length=8)


class User(BaseModel):
    id: int
    name: str
    phone: str
    email: str | None
    logged_at: datetime | None
    status: str
