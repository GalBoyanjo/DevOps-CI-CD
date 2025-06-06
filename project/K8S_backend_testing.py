import sys

import requests

from db_connector import get_user, get_config, get_all_ids

"""
Backend testing on K8S cluster
1. Post a new user data to the REST API using POST method.
2. Submit a GET request to make sure status code is 200 and data equals to the posted data.
3. Check posted data was stored inside DB (users table)
"""

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
HOST = sys.argv[3]


with open('k8s_url.txt', 'r', encoding='utf-16') as url_file:
    k8s_url = url_file.readline().strip('\n')

config = get_config(USERNAME, PASSWORD, HOST)
user_id = 1
user_name = config[2]

# check validation of user_id to insert
ids = get_all_ids(USERNAME, PASSWORD, HOST)
while True:
    if user_id not in ids:
        break
    else:
        user_id += 1

try:
    # Post user data to the REST API
    post_res = requests.post(k8s_url + '/users/' + str(user_id), json={"user_name": user_name})
    # Get user data from REST API and verify response status and match to the post data
    get_res = requests.get(k8s_url + '/users/' + str(user_id))
    if not get_res.ok or get_res.json()['user_name'] != user_name:
        raise Exception("test failed")
    # Get user data from DB(using pymysql)
    if get_user(USERNAME, PASSWORD, HOST, user_id) != user_name:
        raise Exception("test failed")
except Exception as exception:
    raise Exception("test failed", exception)
