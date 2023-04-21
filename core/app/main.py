import logging

from fastapi import FastAPI

from ..ScheduleService.ScheduleService import ScheduleService
from .routers import api_router

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(api_router)
schedule = ScheduleService()


@app.on_event("startup")
def start_scheduler():
    schedule.start()
    logging.info("start sched")


@app.on_event("shutdown")
def stop_scheduler():
    schedule.stop()
