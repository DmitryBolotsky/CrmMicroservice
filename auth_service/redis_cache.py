import redis

REDIS_URL = "redis://redis:6379"

redis_client = redis.Redis.from_url(REDIS_URL)