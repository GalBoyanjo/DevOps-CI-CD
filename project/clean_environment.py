import requests


try:
    requests.get('http://127.0.0.1:5000/stop_server')

    requests.get('http://127.0.0.1:5001/stop_server')
except Exception as exce:
    raise Exception("Environment cleanup failed", exce)
