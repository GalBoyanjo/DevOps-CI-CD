import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}

try:
    requests.get('http://127.0.0.1:5000/stop_server', headers=headers)

    requests.get('http://127.0.0.1:5001/stop_server')
except Exception as exce:
    raise Exception("Environment cleanup failed", exce)
