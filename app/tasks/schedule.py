from app.tasks.worker import celery_app


@celery_app.task(name="periodictask")
def periodic_task():
    print(12345)
