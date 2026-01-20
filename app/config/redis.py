import os
from typing import AsyncGenerator

import redis


class RedisConfig:
    HOST = os.getenv("REDIS_HOST", "auth-center-redis")
    PORT = os.getenv("REDIS_PORT", "6379")
    DB = os.getenv("REDIS_DB", "0")
    URL = f"redis://{HOST}:{PORT}/{DB}"


rc = redis.Redis.from_url(RedisConfig.URL, encoding="utf-8", decode_responses=True)


async def get_redis() -> AsyncGenerator[redis.Redis, None]:
    """
    提供 Redis 连接的依赖注入
    """
    # 直接 yield 全局实例。
    # redis-py 是线程/协程安全的，内部会自动处理连接的获取与释放。
    if rc is None:
        raise RuntimeError("Redis 连接池未初始化")

    yield rc
