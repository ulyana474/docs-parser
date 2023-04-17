from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    author = Column(String)
    title = Column(String, primary_key=True, index=True, unique=True)
    content = Column(String)

    class Config:
        orm_mode = True
