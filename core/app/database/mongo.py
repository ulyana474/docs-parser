import os

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

client = AsyncIOMotorClient(os.environ["MONGODB_URL"])


async def close_mongo_connection():
    client.close()


async def get_database() -> AsyncIOMotorDatabase:
    return client["docs"]
