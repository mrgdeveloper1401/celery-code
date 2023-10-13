from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger


app = Celery('peridoc', broker='amqp://guest:guest@localhost:5672')
app.config_from_object('celery-conf')
logger = get_task_logger(__name__)


@app.task(name='peridoc.show')
def show(name):
    logger.info(name)
    
    
name = show.delay('mohammad',)
