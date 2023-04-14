from typing import Annotated

from fastapi import APIRouter, Depends

from core.app.dependencies.auth import has_access
from core.app.utils.parse import parse_articles

router = APIRouter()


@router.get("/me")
async def me(token: Annotated[str, Depends(has_access)]):
    return {"token": "works"}


@router.get("/parse")
async def parse():
    parsed_data = parse_articles()
    return {"data": "ok"}
