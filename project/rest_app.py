import os
import signal
import sys

import pymysql
from flask import Flask, request, jsonify

from db_connector import add_user, get_user, update_user, delete_user

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]

app = Flask(__name__)

def db_connect(qurey):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user=USERNAME, passwd=PASSWORD,
                           db='db')
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Get user name data from table
    query = qurey
    cursor.execute(query.get_sql())
    user_name = cursor.fetchone()
    cursor.close()
    conn.close()
    return user_name

# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        if get_user(USERNAME, PASSWORD, user_id) == None:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            add_user(USERNAME, PASSWORD, user_id, user_name)
            return {'status id': 'ok', 'user_added': user_name}, 200  # status code
        else:
            return {'status id': 'error', 'reason': 'id already exists'}, 500  # status code

    elif request.method == 'GET':
        user_name = get_user(USERNAME, PASSWORD, user_id)
        # query = get_user(user_id)
        # user_name = db_connect(query)
        if user_name != None:
            return {'status id': 'ok', 'user_name': user_name}, 200  # status code
            # return {'status id': 'ok', 'user_name': user_name[0]}, 200  # status code
        else:
            return {'status id': 'error', 'reason': 'no such id'}, 500  # status code

    elif request.method == 'PUT':
        if get_user(USERNAME, PASSWORD, user_id) != None:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            update_user(USERNAME, PASSWORD, user_id, user_name)
            return {'status id': 'ok', 'user_updated': user_name}, 200  # status code
        else:
            return {'status id': 'error', 'reason': 'no such id'}, 500  # status code

    elif request.method == 'DELETE':
        user_name = get_user(USERNAME, PASSWORD, user_id)
        if get_user(USERNAME, PASSWORD, user_id) != None:
            delete_user(USERNAME, PASSWORD, user_id)
            return {'status id': 'ok', 'user_deleted': user_name}, 200  # status code
        else:
            return {'status id': 'error', 'reason': 'no such id'}, 500  # status code


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


app.run(host='0.0.0.0', debug=True, port=5000)
