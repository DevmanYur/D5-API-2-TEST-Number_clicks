import requests
import json

url = 'https://api-ssl.bitly.com/v4/user'
headers = {
     'Authorization': 'Bearer d8f3784dc29d4dbab3752c20b2076bf878e9e524',
 }
response = requests.get(url, headers=headers)
print(response.json())

