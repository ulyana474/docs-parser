from typing import List

from bson.objectid import ObjectId
from fastapi import Body, Depends, Response, status, HTTPException
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient

from core.app.database.mongo import get_database
from core.app.schemas.articles import Article
from core.app.utils.parse import parse_articles

from .base import BaseRepository


class Repository(BaseRepository):

    @staticmethod
    def get_collection(db: AsyncIOMotorClient = Depends(get_database)):
        collection = db.get_collection('docs')
        return collection

    @staticmethod
    async def get(db: AsyncIOMotorClient = Depends(get_database)) -> List:
        collection = Repository.get_collection(db)
        cursor = collection.find()
        docs_to_show = []
        async for document in cursor:
            document["_id"] = str(document["_id"])  # ObjectId for Mongo
            docs_to_show.append(document)
        return docs_to_show

    @staticmethod
    async def get_by_id(docs_id: str, db: AsyncIOMotorClient = Depends(get_database)):
        collection = Repository.get_collection(db)
        if (existing_docs := await collection.find_one({'_id': ObjectId(docs_id)})) is not None:
            return existing_docs
        else:
            raise HTTPException(status_code=404, content="not found")  

    @staticmethod
    async def create(db: AsyncIOMotorClient = Depends(get_database)):
        collection = Repository.get_collection(db)
        new_docs = parse_articles()
        for doc in new_docs:
            await collection.insert_one(jsonable_encoder(doc))
        return new_docs

    @staticmethod
    async def update(docs_id: str, docs: Article = Body(...), db: AsyncIOMotorClient = Depends(get_database)):
        collection = Repository.get_collection(db)
        docs = {k: v for k, v in docs.dict().items() if v is not None}
        print(docs)
        update_result = await collection.update_one({"_id": docs_id}, {"$set": docs})
        return update_result

    @staticmethod
    async def delete(db: AsyncIOMotorClient = Depends(get_database)):
        pass

    @staticmethod
    async def delete_all(db: AsyncIOMotorClient = Depends(get_database)):
        collection = Repository.get_collection(db)
        result = await collection.delete_many({})
        return result.deleted_count
