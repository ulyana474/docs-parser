from fastapi import FastAPI
from .routers import router
from auth.app.models import user
# from sqlmodel import SQLModel

# SQLModel.metadata.create_all()

app = FastAPI()
app.include_router(router.api_v1_router)

