from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config import CORS
from app.config.database import engine
from app.config.log import setup_logging
from app.config.redis import rc
from app.apis.auth import router as auth_router
from app.apis.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- 【启动阶段】 ---
    setup_logging()

    # Postgres
    try:
        async with engine.connect() as conn:
            await conn.exec_driver_sql("SELECT 1")
        print("SQLAlchemy 连接池初始化成功，已连接到 PostgreSQL")
    except Exception as e:
        print(f"数据库连接失败: {e}")
        raise e

    # Redis
    rc.ping()
    print("Redis 连接池初始化成功")

    yield  # 运行期间

    # --- 【关闭阶段】 ---
    await engine.dispose()
    rc.close()


fast_app = FastAPI(lifespan=lifespan)

fast_app.add_middleware(CORSMiddleware, **CORS)


fast_app.include_router(auth_router, prefix='/auth', tags=['auth'])
fast_app.include_router(user_router, prefix='/user', tags=['user'])


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(fast_app, host='127.0.0.1', port=8000)
