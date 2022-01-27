import requests

url = "https://futdb.app/api/players"

r = requests.get(url, headers={'accept': 'application/json', 'X-AUTH-TOKEN': ''})

print(r.status_code)
print(r.content)

