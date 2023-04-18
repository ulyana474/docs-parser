from pydantic import BaseModel, Field


class Article(BaseModel):
    author: str | None = None
    title: str | None = None
    content: str | None = None
