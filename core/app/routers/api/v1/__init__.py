from fastapi import APIRouter
from . import articles

v1_router = APIRouter(prefix='/v1')
v1_router.include_router(articles.router)
