import redis.asyncio as redis
from app.core.config import settings

class RedisManager:
    def __init__(self):
        self.redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)

    async def acquire_lock(self, lock_key: str, expire_seconds: int = 10) -> bool:
        """
        Attempts to set a distributed lock in Redis. 
        Returns True if acquired successfully, False if already locked.
        """
        acquired = await self.redis_client.set(lock_key, "locked", nx=True, ex=expire_seconds)
        return bool(acquired)

    async def release_lock(self, lock_key: str):
        """Releases the Redis distributed lock."""
        await self.redis_client.delete(lock_key)

redis_manager = RedisManager()