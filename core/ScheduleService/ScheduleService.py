import logging
from apscheduler.schedulers.background import BackgroundScheduler

logging.basicConfig(level=logging.INFO)

class ScheduleService:

    scheduler = BackgroundScheduler()

    def my_task(self):
        logging.info("Hello, world!")

    def start(self):
        self.scheduler.add_job(self.my_task, "interval", seconds=5)
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()
        