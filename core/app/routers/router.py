from .api.v1 import articles
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/docs", tags=["docs"])

router.include_router(articles.router)

