import requests
import os
from dotenv import load_dotenv


def get_short_url(long_url, token):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    body = {
        "long_url": long_url,
    }
    response = requests.post(
        url, 
        headers=headers, 
        json=body,
    )
    response.raise_for_status()
    return response.json()['id']


def get_clicks(shot_url, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{shot_url}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(bitlink, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.environ.get("BITLY_GENERIC_ACCESS_TOKEN")
    user_url = input('Введите ссылку: ')
    if is_bitlink(user_url, bitly_token):
        try:
            print('Количество переходов по вашей ссылке: ', get_clicks(user_url, bitly_token))
        except requests.exceptions.HTTPError:
            print('не удалось получить короткую ссылку')
    else:
        try:
            print('Битлинк: ', get_short_url(user_url, bitly_token))
        except requests.exceptions.HTTPError:
            print('не удалось получить количество переходов по короткой ссылке')


if __name__ == '__main__':
    main()
