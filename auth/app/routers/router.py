from fastapi import APIRouter

from .api.v1 import user

api_v1_router = APIRouter(prefix="/api/v1/users", tags=["users"])

api_v1_router.include_router(user.router)
