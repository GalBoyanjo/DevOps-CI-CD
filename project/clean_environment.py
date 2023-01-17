import requests

# Terminate REST API server
try:
    requests.get('http://127.0.0.1:5000/stop_server')
except ConnectionResetError as conn_exce:
    raise Exception("Connection error - (connection probably already closed):\n", conn_exce)
except Exception as exce:
    raise Exception("Environment cleanup failed\n", exce)

# Terminate web app server
try:
    requests.get('http://127.0.0.1:5001/stop_server')
except ConnectionResetError as conn_exce:
    raise Exception("Connection error - (connection probably already closed):\n", conn_exce)
except Exception as exce:
    raise Exception("Environment cleanup failed\n", exce)
