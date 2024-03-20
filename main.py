
import requests

def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {"long_url": url}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)
    return response.json()['link']



token = 'd8f3784dc29d4dbab3752c20b2076bf878e9e524'
url = 'https://ya.ru/'
print('Битлинк', shorten_link(token, url))




