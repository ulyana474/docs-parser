from pydantic import BaseModel
from uuid import UUID
from typing import Union

class Article(BaseModel):
    id: UUID
    author: Union[str | list] = None
    title: str
    content: str