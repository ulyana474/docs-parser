from pydantic import BaseModel
from uuid import UUID


class Article(BaseModel):
    id: UUID
    author: str | list = None
    title: str
    content: str