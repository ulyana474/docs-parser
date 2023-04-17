import os
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient

client = AsyncIOMotorClient(os.environ['MONGODB_URL'])


async def close_mongo_connection():
    client.close()


async def get_database() -> AsyncIOMotorDatabase:
    return client['docs']
