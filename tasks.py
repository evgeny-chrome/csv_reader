from app import celery
from utils import sum_columns


@celery.task(bind=True, max_retries=3)
def sum_columns_task(self, file: str = '') -> dict:
    try:
        result = sum_columns(file=file)
    except:
        self.retry(countdown=1)
        result = 'file has not been read'
        print('retry')
    return result
