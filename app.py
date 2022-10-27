from celery import Celery
from flask import Flask
from celery_config import brocker_url, result_backend_url

app_name = 'csv_app'

app = Flask(app_name)

celery = Celery(
    app_name,
    backend=result_backend_url,
    broker=brocker_url,
    imports=['tasks']
)

celery.conf.update(app.config)


class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

celery.Task = ContextTask
