from celery import Celery
from celery.schedules import crontab


app = Celery('periodic_task', broker='amqp://guest:guest@localhost:5672')
app.config_from_object('celery_conf')


@app.task
def show(name):
    return f'hello {name}'