from celery import Celery
from ser import Person


app = Celery('serapp', broker='amqp://guest:guest@localhost:5672//', backend='rpc://')
app.config_from_object('ser_config')



@app.task(bind=True)
def call(self, Person):
    return Person.show()

p1 = Person('John', 'Doe', 30)
result = call.delay(p1)
# print(result.get())