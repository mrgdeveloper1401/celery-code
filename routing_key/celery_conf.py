from celery import Celery
from kombu import Exchange, Queue


defult_exchange = Exchange('default', type='direct')
media_exchange = Exchange('media', type='direct')

task_queus = (
    Queue('default', defult_exchange, routing_key='default'),
    Queue('media', media_exchange, routing_key='media'),
    Queue('image', defult_exchange, routing_key='image'),
)

task_defult_queue = 'default'
task_defult_exchange = 'default'
task_defult_routing_key = 'default'

task_routes = {
    'routing.add': {
        'queue': 'media'
    },
    'routing.mull': {
        'queue':'image'
    },
}