from fastapi import FastAPI

from .routers.router import router
from ..ScheduleService.ScheduleService import ScheduleService

app = FastAPI()
app.include_router(router)
schedule = ScheduleService()


@app.on_event("startup")
def start_scheduler():
    schedule.start()


@app.on_event("shutdown")
def stop_scheduler():
    schedule.stop()
