
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Hello This is a Dev platform!'

application = default_app()

