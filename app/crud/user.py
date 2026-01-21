from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User


async def get_user_by_phone(db: AsyncSession, phone: str) -> User | None:
    stmt = select(User).where(User.phone == phone)
    result = await db.execute(stmt)
    return result.scalars().first()


async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    return result.scalars().first()
