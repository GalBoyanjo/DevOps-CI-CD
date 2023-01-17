import requests

from requests.exceptions import ChunkedEncodingError

# Terminate REST API server
try:
    requests.get('http://127.0.0.1:5000/stop_server')
except ChunkedEncodingError as conn_exce:
    print("Connection error - (connection probably already closed):", conn_exce)
except Exception as exce:
    print("Environment cleanup failed", exce)

# Terminate web app server
try:
    requests.get('http://127.0.0.1:5001/stop_server')
except ChunkedEncodingError as conn_exce:
    print("Connection error - (connection probably already closed):", conn_exce)
except Exception as exce:
    print("Environment cleanup failed", exce)
