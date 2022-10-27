from celery.result import AsyncResult
from flask import jsonify
from flask.views import MethodView

from tasks import sum_columns_task
from app import celery


class SumView(MethodView):

    def get(self, task_id):
        task = AsyncResult(task_id, app=celery)
        return jsonify({'status': task.status,
                        'result': str(task.result)})
    def post(self, file):
        task = sum_columns_task.delay(file)
        return jsonify(
            {'task_id': task.id}
        )
