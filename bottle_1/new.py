
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():

    return 'Made some changes in development server'



application = default_app()

