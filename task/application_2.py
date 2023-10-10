from celery import Celery
from celery.utils.log import get_task_logger


app = Celery('config', broker='amqp://guest:guest@localhost:5672', backend='rpc://')
logger = get_task_logger(__name__)
# app.config_from_object('celery_confcelery_conf')


@app.task(name='application_2.mul')
def mul(a, b):
    return a * b

