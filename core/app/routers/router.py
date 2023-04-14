from fastapi import APIRouter

from .api.v1 import articles

router = APIRouter(prefix="/api/v1/docs", tags=["docs"])

router.include_router(articles.router)
