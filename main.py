
import requests


def count_clicks(token, bitlink):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    params = (
        ('unit', 'month'),
        ('units', '1'),
        ('unit_reference', '2006-01-02T15:04:05-0700'),
    )

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks',
                            headers=headers,
                            params=params)
    response.raise_for_status()
    count_clicks = response.json()
    return count_clicks


def shorten_link(token, link):
    response_link = requests.post(link)
    response_link.raise_for_status()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {"long_url": link}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink

token = 'd8f3784dc29d4dbab3752c20b2076bf878e9e524'
user_input = input("Введите ссылку для сокращения: ")


try:
  bitlink = shorten_link(token, user_input)
  print('Битлинк', bitlink)
  count_clicks(token, bitlink)

except Exception as e:
  print('Ошибка при загрузке страницы: ' + str(e))

# url = 'https://ya.ru/'
# url = 'https://ya888.ru/'





