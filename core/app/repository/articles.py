from fastapi import status, Depends, Response
from typing import List
from .base import BaseRepository
from core.app.utils.parse import parse_articles
from core.app.database.mongo import get_database
from motor.motor_asyncio import AsyncIOMotorClient
from core.app.models.articles import Article
from fastapi.encoders import jsonable_encoder


class Repository(BaseRepository):

    @staticmethod
    async def get(db: AsyncIOMotorClient = Depends(get_database)) -> List:
        collection = db.get_collection('docs')
        cursor = collection.find()
        docs_to_show = []
        async for document in cursor:
            document["_id"] = str(document["_id"])
            docs_to_show.append(document)
        return docs_to_show

    @staticmethod
    async def create(db: AsyncIOMotorClient = Depends(get_database)):
        collection = db.get_collection('docs')
        new_docs = parse_articles()
        for doc in new_docs:
            await collection.insert_one(jsonable_encoder(doc))
        return new_docs

    @staticmethod
    async def update(db: AsyncIOMotorClient = Depends(get_database)):
        pass

    @staticmethod
    async def delete(db: AsyncIOMotorClient = Depends(get_database)):
        pass

    @staticmethod
    async def delete_all(db: AsyncIOMotorClient = Depends(get_database)):
        collection = db.get_collection('docs')
        result = await collection.delete_many({})
        return result.deleted_count
