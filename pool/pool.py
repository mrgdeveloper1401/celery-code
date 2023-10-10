from celery import Celery


app = Celery('pool', broker='amqp://guest:guest@localhost:5672//', backend='rpc://')


@app.task
def add(a, b):
    return a + b