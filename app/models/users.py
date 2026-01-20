import enum

from sqlalchemy import Enum, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class UserStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(32), nullable=False)
    phone: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(128), nullable=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)

    logged_at = Mapped[DateTime] = mapped_column(nullable=False)
    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus, native_enum=True),
        server_default=UserStatus.ACTIVE.value
    )
