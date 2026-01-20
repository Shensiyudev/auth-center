
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    created_at = Mapped[DateTime] = mapped_column(
        DateTime,
        insert_default=func.now(),
        default=func.now()
    )
    updated_at = Mapped[DateTime] = mapped_column(
        DateTime,
        insert_default=func.now(),
        default=func.now(),
        onupdate=func.now()
    )
