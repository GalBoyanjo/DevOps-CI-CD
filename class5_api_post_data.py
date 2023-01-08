import requests
res = requests.post('http://127.0.0.1:5000/data/3', json={"user_name":"arian"})
if res.ok:
    print(res.json())