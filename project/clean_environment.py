import requests


try:
    requests.get('http://127.0.0.1:5000/stop_server')

except Exception as rest_exce:
    raise Exception("rest_app cleanup failed", rest_exce)
try:
    requests.get('http://127.0.0.1:5001/stop_server')
except Exception as web_exce:
    raise Exception("web_app cleanup failed", web_exce)