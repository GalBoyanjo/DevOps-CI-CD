import requests


try:
    print('5000 before')
    rest_req = requests.get('http://127.0.0.1:5000/stop_server')
    print('5000 after')
    print(rest_req)
    print('5001 before')
    web_req = requests.get('http://127.0.0.1:5001/stop_server')
    print('5001 after')
    print(web_req)
except Exception as exce:
    raise Exception("Environment cleanup failed", exce)
