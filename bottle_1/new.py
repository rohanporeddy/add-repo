
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
<<<<<<< HEAD
    return 'Hello from Bottle!'
=======
    return 'Changes done in Dev'
>>>>>>> 504d44db7694e45bf837b5fd5e646b529f26e21e

application = default_app()

