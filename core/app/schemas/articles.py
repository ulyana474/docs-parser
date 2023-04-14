from uuid import UUID

from pydantic import BaseModel


class Article(BaseModel):
    id: UUID
    author: str | list = None
    title: str
    content: str
