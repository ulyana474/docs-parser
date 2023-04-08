from fastapi import FastAPI
from .routers import router
from auth.app.models import user

app = FastAPI()
app.include_router(router.api_v1_router)

