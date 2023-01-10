import requests


def post_req(user_id: str, user_name: str):
    post_res = requests.post('http://127.0.0.1:5000/users/' + user_id, json={"user_name": user_name})
    if post_res.ok:
        print(post_res.json())


def put_req(user_id: str, user_name: str):
    put_res = requests.put('http://127.0.0.1:5000/users/' + user_id, json={"user_name": user_name})
    if put_res.ok:
        print(put_res.json())


def delete_req(user_id: str):
    delete_res = requests.delete('http://127.0.0.1:5000/users/' + user_id)
    if delete_res.ok:
        print(delete_res.json())

