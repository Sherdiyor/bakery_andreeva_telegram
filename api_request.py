import requests

API_TOKEN = '74100620b888a8249a0321ab69eff55d247a28d1'
URL = 'http://127.0.0.1:8000/api/'


def get_forms():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {API_TOKEN}'
    }
    response = requests.get(URL + 'form/', headers=headers)
    res = response.json()
    return res


def delete_form(id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {API_TOKEN}'
    }
    requests.delete(URL + f'form/{int(id)}/', headers=headers)


# print(get_forms())
