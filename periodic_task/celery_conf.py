from celery import Celery
from celery.schedules import crontab


beat_schedules = {
    'call_show_every_one_minute': {
        'task': 'periodic_task.show',
        'schedules': crontab(minute='*/1'),
        'args': ('mohammad',),
    },
}