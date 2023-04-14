from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String, index=True, unique=True)
    content = Column(String)

    class Config:
        orm_mode = True
