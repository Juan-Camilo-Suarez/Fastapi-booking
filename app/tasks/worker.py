from celery import Celery
from celery.schedules import crontab

from app.config import settings

celery_app = Celery(
    'tasks',
    broker=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}',
    include=["app.tasks.tasks",
             "app.tasks.schedule"],
)

# celery bit schedule
celery_app.conf.beat_schedule = {
    "luboe-nazvanie": {
        "task": "periodict task",
        "schedule": crontab(minute="5", hour="11"),
    }
}
