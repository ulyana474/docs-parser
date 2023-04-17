from pydantic import BaseModel, Field


class Article(BaseModel):
    author: str | list = None
    title: str
    content: str
