import argparse
import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


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
    parse_url = urlparse(shot_url)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parse_url.netloc}{parse_url.path}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(bitlink, token):
    parse_url = urlparse(bitlink)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parse_url.netloc}{parse_url.path}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.environ.get("BITLY_TOKEN")
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='url адрес')
    args = parser.parse_args()
    if is_bitlink(args.url, bitly_token):
        try:
            print('Количество переходов по вашей ссылке: ', get_clicks(args.url, bitly_token))
        except requests.exceptions.HTTPError:
            print('не удалось получить количество переходов по короткой ссылке')
    else:
        try:
            print('Битлинк: ', get_short_url(args.url, bitly_token))
        except requests.exceptions.HTTPError:
            print('не удалось получить короткую ссылку')


if __name__ == '__main__':
    main()
