from celery import Celery
from celery.schedules import crontab
from periodic_tasks import app


beat_schedule = {
    'call_show_every_one_minute': {
        'task': 'peridoc.show',
        'schedule': crontab(minute='*/1'),
        'args': ('mohammad',),
    },
}
app.conf.timezone = 'Asia/Tehran'