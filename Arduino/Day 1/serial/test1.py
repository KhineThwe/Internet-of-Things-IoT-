import requests
url="http://192.168.0.20"
r=requests.get(url)
print(r.json())