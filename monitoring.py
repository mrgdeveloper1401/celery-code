from celery import Celery
from celery.utils.log import get_task_logger



app = Celery('monitoring', broker='amqp://guest:guest@localhost:5672/', backend='rpc://')


@app.task
def mul(a,b):
    return (a * b)