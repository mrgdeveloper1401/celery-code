from celery import Celery
from celery.utils.log import get_task_logger
import logging

app = Celery('application', broker='amqp://vpn:vpnvpn@localhost:5672/vpn_vhost', backend='rpc://')
logger = get_task_logger(__name__)

@app.task
def add(a,b):
    return a + b

# @app.task(name='application.add')
# def add(a,b):
#     return a+b




# @app.task(bind=True, default_retry_delay=10, max_retries=5)
# def add(self, a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         logger.info('sorry.............')
#         self.retry(countdown=10)