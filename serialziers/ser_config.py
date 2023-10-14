from serapp import app


app.conf.update(
    task_serializer= 'pickle',
    result_serializer= 'pickle',
    accept_content = ['pickle',],
)