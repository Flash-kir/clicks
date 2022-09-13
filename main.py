import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json
from urllib.parse import urlparse

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DEFAULT_GROUP_GUID = os.environ.get("DEFAULT_GROUP_GUID")
GENERIC_ACCESS_TOKEN = os.environ.get("GENERIC_ACCESS_TOKEN")

def get_short_url(long_url, token):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    url_headers = {
        'Authorization': token,
    }
    url_params = {
        "long_url": long_url,
        "domain": "bit.ly",
        "group_id": DEFAULT_GROUP_GUID,
    }
    response = requests.post(
        url, 
        headers=url_headers, 
        data=json.dumps(url_params),
    )
    response.raise_for_status()
    return(response.json()['id'])

def get_user_url():
    return input('Введите ссылку: ')

def get_clicks(shot_url, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{shot_url}/clicks/summary'
    url_headers = {
        'Authorization': token,
    }
    response = requests.get(url, headers=url_headers)
    response.raise_for_status()
    return response.json()['total_clicks']

def is_bitlink(url):
    parsed = urlparse(url)
    if parsed.netloc:
        return False
    return True
    
def main():
    try:
        user_url = get_user_url()
        if is_bitlink(user_url):
            print('Количество переходов по вашей ссылке: ', get_clicks(user_url, GENERIC_ACCESS_TOKEN))
        else:
            print('Битлинк: ', get_short_url(user_url, GENERIC_ACCESS_TOKEN))
    except requests.exceptions.HTTPError:
        print('ссылка введена не корректно или не найдена')

if __name__ == '__main__':
    main()
