from celery import Celery
from celery.utils.log import get_task_logger


app = Celery('binds', broker='amqp://vpn:vpnvpn@localhost:5672/vpn_vhost', backend='rpc://')
logger = get_task_logger(__name__)


# @app.task(bind=True)
# def dev(self, a, b):
#     print(self)
#     print(self.request)
#     return a / b
        
        
# @app.task(bind=True)
# def dev(self, a, b):
#     try: 
#         return a / b
#     except ZeroDivisionError:
#         logger.info('ziro division error')
#         print('retry task afte 10 seconds')
#         self.retry(countdown=10)



@app.task(bind=True)
def dev(self, a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        logger.warning('ziro division error')
        logger.info('retry task after 10 seconds')
        self.retry(countdown=10, max_retries=5)