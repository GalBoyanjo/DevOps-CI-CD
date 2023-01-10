import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

try:
    requests.get('http://127.0.0.1:5000/stop_server', headers=headers)

    requests.get('http://127.0.0.1:5001/stop_server', headers=headers)
except Exception as exce:
    raise Exception("Environment cleanup failed", exce)
