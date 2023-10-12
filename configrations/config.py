from celery import Celery



app = Celery('config', broker='amqp://guest:guest@localhost:5672/', backend='rpc://')

