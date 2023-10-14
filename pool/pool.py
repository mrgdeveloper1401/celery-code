from celery import Celery
from time import sleep


app = Celery('pool', broker='amqp://guest:guest@localhost:5672//', backend='rpc://')


@app.task
def add(a, b):
    sleep(2)
    return a + b