from celery import Celery

result_backend = 'rpc://'

app = Celery('celery_conf', broker='amqp://guest:guest@localhost:5672')

app.conf.update(
    task_time_limit = 60,
    task_soft_limit = 50,
    worker_concurrency = 3,
    worker_prefetch_multiplier = 1,
    task_ignore_result = True,
    task_acks_late = True,
)