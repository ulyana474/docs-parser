from typing import Annotated
from fastapi import APIRouter, Depends
from core.app.dependencies.auth import has_access

router = APIRouter()


@router.get('/me')
async def me(token: Annotated[str, Depends(has_access)]):
    return {"token": "works"}