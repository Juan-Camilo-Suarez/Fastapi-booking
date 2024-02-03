from celery import Celery

celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379',
    include=["app.tasks.tasks"],
)
