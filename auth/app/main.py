from fastapi import FastAPI

from auth.app.models import user

from .routers import router

app = FastAPI()
app.include_router(router.api_v1_router)
