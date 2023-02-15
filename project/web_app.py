import sys

from flask import Flask

from db_connector import get_user

import os
import signal

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
HOST = sys.argv[3]

app = Flask(__name__)


@app.route("/users/get_user_name/<user_id>")
def get_user_name(user_id):
    user_name = get_user(USERNAME, PASSWORD, HOST, user_id)
    if user_name == None:
        return "<H1 id='error'>no such user: " + user_id + "</H1>"
    else:
        return "<H1 id='user'>" + user_name + "</H1>"


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.errorhandler(404)
def page_not_found(e):
    return "<H1> 404 </H1><p>Oops!</p>", 404


app.run(host='0.0.0.0', debug=True, port=5001)
