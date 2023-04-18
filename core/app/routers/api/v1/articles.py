from typing import Annotated, List

from fastapi import APIRouter, Depends, status, Response
from fastapi.responses import JSONResponse
from core.app.dependencies.auth import has_access
from core.app.utils.parse import parse_articles
from core.app.repository.articles import Repository
from core.app.schemas.articles import Article
from core.app.repository.articles import Repository


router = APIRouter()


# @router.get("/me")
# async def me(token: Annotated[str, Depends(has_access)]):
#     return {"token": "works"}


@router.get("/parse")
async def parse():
    parsed_data = parse_articles()
    print(parsed_data)
    return {"data": "ok"}


@router.get("/get-docs", status_code=status.HTTP_200_OK)
async def get_docs(docs=Depends(Repository.get)):
    return {'docs': docs}


@router.get("/get-docs-by-id/{docs_id}", status_code=status.HTTP_200_OK, response_model=Article)
async def get_docs_by_id(docs_id: str, docs=Depends(Repository.get_by_id)):
    return docs


@router.post("/insert-docs", status_code=status.HTTP_201_CREATED)
async def insert_docs(res=Depends(Repository.create)):
    return {'inserted': res}


@router.put("/update-docs/{docs_id}", status_code=status.HTTP_200_OK, response_model=Article)
async def update_docs(docs_id: str, docs=Depends(Repository.update)):
    return {'updated': docs}


@router.delete("/delete-all-docs", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_docs(res=Depends(Repository.delete_all)):
    return {'deleted': res}

