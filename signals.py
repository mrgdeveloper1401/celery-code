from celery import Celery, signals
from celery.signals import after_setup_logger


app = Celery('signals', broker='amqp://guest:guest@localhost:5672')
app.config_from_object('celery_conf')

@app.task
def add(a, b):
    return a + b

@app.task
def mul(a, b):
    return a * b


@signals.task_prerun.connect
def show(sender=None, **kwargs):
    print('tsk before run ')
    print(sender)
    print(kwargs)