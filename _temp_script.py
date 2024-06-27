import requests

url = 'http://127.0.0.1:8000/token/'

r = requests.post(url, data={
  'username': 'albert',
  'password': 'a1d2m3i4n'
  }
)


print(r.json())