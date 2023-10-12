from celery import Celery
from celery.utils.log import get_task_logger


app = Celery('keep_res', broker='amqp://guest:guest@localhost:5672/', backend='rpc://')
logger = get_task_logger(__name__)


@app.task(name='keep_res.mul')
def mul(a, b):
    return a * b


@app.task(name='keep_res.div', default_retry_delay=10)
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.error('ziro division error')
        logger.info('retry task after 10 seconds')
        