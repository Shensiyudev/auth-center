from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.utils import PasswordManager


class UserStatus:
    ACTIVE = "active"
    INACTIVE = "inactive"


class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(32), nullable=False)
    phone: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(128), nullable=True)

    logged_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    status: Mapped[str] = mapped_column(String(16), server_default=UserStatus.ACTIVE, nullable=False)

    _password: Mapped[str] = mapped_column("password", String(256), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plain_password: str):
        # 赋值时自动加密
        self._password = PasswordManager.encrypt(plain_password)

    def values(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "logged_at": self.logged_at,
            "status": self.status
        }
