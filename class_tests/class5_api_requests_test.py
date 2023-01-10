# import requests
# res = requests.get('https://google.com')
# if res.ok:
#     print(res.content)
#


import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount=1"

payload = {}
headers = {"apikey": "2QGjX7OvxT5VFeinxMOmUCAoBEm7bkE8"}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()

print(result)
