from celery import Celery
from kombu import Exchange, Queue


default_exchange = Exchange('default', type='direct')
math_exchange = Exchange('math', type='direct')

task_queues = {
    'default': Queue('default', default_exchange, routing_key='default'),
    'add': Queue('add', math_exchange, routing_key='add'),
    'mull': Queue('mull', math_exchange, routing_key='mull'),
}

task_default_echange = 'default'
task_default_queue = 'default'
task_default_routing_key = 'default'

task_routes = {
    'routing.add': {'queue': 'add'},
    'routing.mull': {'queue':'mull'},
}