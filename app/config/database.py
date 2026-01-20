import os

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


class PostgresConfig:
    HOST = os.getenv("POSTGRES_HOST", "postgres")
    PORT = os.getenv("POSTGRES_PORT", "5432")
    USER = os.getenv("POSTGRES_USER", "postgres")
    PASSWORD = os.getenv("POSTGRES_PASSWORD", "123456")
    DB = os.getenv("POSTGRES_DB", "rag")
    URL = f"postgresql+psycopg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"


# 创建异步引擎 (内建连接池管理)
engine = create_async_engine(PostgresConfig.URL, echo=True)

# 创建 Session 工厂
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# 依赖注入函数：每个请求获取一个独立 Session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
