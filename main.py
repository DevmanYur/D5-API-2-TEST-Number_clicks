
import requests


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
    bitlink = response.json()['link']
    return bitlink

token = 'd8f3784dc29d4dbab3752c20b2076bf878e9e524'
# url = 'https://ya.ru/'
# url = 'https://ya888.ru/'
user_input = input("Введите ссылку для сокращения: ")


try:
  bitlink = shorten_link(token, user_input)
  print('Битлинк', bitlink)
except Exception as e:
  print('Ошибка при загрузке страницы: ' + str(e))



