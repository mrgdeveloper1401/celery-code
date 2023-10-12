from celery import Celery


app = Celery('config', broker='amqp://guest:guest@localhost:5672/', backend='rpc://')
app.config_from_object('celery_conf')



@app.task(name='configs.mull')
def mull(a, b):
    return a * b