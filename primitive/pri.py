from celery import Celery, chain, signature, group, chunks


app = Celery('pri', broker='amqp://guest:guest@localhost:5672', backend='rpc://')


@app.task(name='primitive.mull')
def mull(a, b):
    return a * b


@app.task(name='primitive.add')
def add(a, b):
    return a + b

# result = chain(mull.s(4,6), add.s(10,))
# print(result().parent.get())

# result = group(mull.s(10,7), add.s(10, 20))
# print(result().get())

# result = group(mull.s(10,7), add.s(10, 20))(mull.s(10, 20))
# print(result().get())

# result = add.chunks(zip(range(100), range(100)), 10)
# print(result().get())


