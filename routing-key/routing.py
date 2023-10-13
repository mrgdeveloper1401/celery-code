from celery import Celery, signals


app = Celery('routing', broker='amqp://guest:guest@localhost:5672//', backend='rpc://')
app.config_from_object('celery_conf')


@app.task(name='routing.add')
def add(a, b):
    return a + b


@app.task(name='routing.mull')
def mull(a, b):
    return a * b


@signals.task_postrun.connect
def show_info(sender=None, **kwargs):
    print(sender.request)
    