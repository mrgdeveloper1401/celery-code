from celery import Celery
from celery.utils.log import get_task_logger
from celery import signature


app = Celery('signature', broker='amqp://guest:guest@localhost:5672', backend='rpc://')
logger = get_task_logger(__name__)
app.config_from_object('celery_conf')


@app.task
def mull(a, b):
    return a * b

# result = mull.signature((4, ))
# result.delay(20)

@app.task
def add(a, b):
    return a + b
result = mull.apply_async((4, 5), link=add.si(2, 10))