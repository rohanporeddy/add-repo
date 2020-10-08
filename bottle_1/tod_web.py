from bottle import get, post, run, template, request, debug, redirect
import os
import sqlite3
from bottle import get, post, template, request, redirect

# are we executing at PythonAnywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ

assert ON_PYTHONANYWHERE == False

if ON_PYTHONANYWHERE:
    pass
else:
    # on the development environment, import the development server
    from bottle import run, debug


@get('/')
def get_show_list():
@@ -25,6 +38,11 @@ def post_new_item():
    cursor.close()
    #return "The new item is [" + new_item + "]..."
    redirect("/")

debug(True)
run(host='localhost', port=8080)


if ON_PYTHONANYWHERE:
    pass
else:
    # on the development environment, run the development server
    debug(True)
    run(host='localhost', port=8080)