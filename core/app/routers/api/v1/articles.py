from typing import Annotated, List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse

from core.app.dependencies.auth import has_access
from core.app.repository.articles import Repository
from core.app.schemas.articles import Article
from core.app.utils.parse import parse_articles

router = APIRouter(prefix='/docs', tags=["docs"])


@router.get("/me")
async def me(token: Annotated[str, Depends(has_access)]):
    return {"token": "works"}


@router.get("/parse")
async def parse():
    parsed_data = parse_articles()
    print(parsed_data)
    return {"data": "ok"}


@router.get("/", status_code=status.HTTP_200_OK)
async def get_docs(docs=Depends(Repository.get)):
    return {"docs": docs}


@router.get(
    "/{docs_id}", status_code=status.HTTP_200_OK, response_model=Article
)
async def get_docs_by_id(docs_id: str, docs=Depends(Repository.get_by_id)):
    return docs


@router.post("/", status_code=status.HTTP_201_CREATED)
async def insert_docs(res=Depends(Repository.create)):
    return {"inserted": res}


@router.put("/{docs_id}", status_code=status.HTTP_200_OK)
async def update_docs(docs_id: str, docs=Depends(Repository.update)):
    return {"updated": docs}


@router.delete("/{docs_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_docs_by_id(docs_id: str, res=Depends(Repository.delete_by_id)):
    return {"deleted": res}


@router.delete("/all", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_docs(res=Depends(Repository.delete_all)):
    return {"deleted": res}
