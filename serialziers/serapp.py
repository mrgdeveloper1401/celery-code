from celery import Celery
from ser import Person


app = Celery('serapp', broker='amqp://guest:guest@localhost:5672//', backend='rpc://')

app.conf.update(
    task_serializer= 'pickle',
    result_serializer= 'pickle',
    accept_content = ['application/x-python-serialzie'],
)

p1 = Person('John', 'Doe', 30)
@app.task(bind=True)
def call(Person):
    return Person.show()

result = call.delay(p1)
print(result.get)