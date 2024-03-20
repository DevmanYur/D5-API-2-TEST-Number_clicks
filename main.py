# import requests
#
# url = 'https://api-ssl.bitly.com/v4/user'
# headers = {
#     'Authorization': 'Bearer d8f3784dc29d4dbab3752c20b2076bf878e9e524',
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.json())


import requests

headers = {
    'Authorization': 'Bearer d8f3784dc29d4dbab3752c20b2076bf878e9e524',
    'Content-Type': 'application/json',
}

data = '{ "long_url": "https://ya.ru/" }'

response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

print(response.json())





