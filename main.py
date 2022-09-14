import requests
import os
from dotenv import load_dotenv

def get_short_url(long_url, token):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    url_headers = {
        'Authorization': token,
    }
    url_params = {
        "long_url": long_url,
    }
    response = requests.post(
        url, 
        headers=url_headers, 
        json=url_params,
    )
    response.raise_for_status()
    return response.json()['id']
    
def get_clicks(shot_url, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{shot_url}/clicks/summary'
    url_headers = {
        'Authorization': token,
    }
    response = requests.get(url, headers=url_headers)
    response.raise_for_status()
    return response.json()['total_clicks']

def is_bitlink(bitlink, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    url_headers = {
        'Authorization': token,
    }
    response = requests.get(url, headers=url_headers)
    try:
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError:
        return False
    
def main():
    '''ya.ru = bit.ly/3Ue0Mdc'''
    load_dotenv()
    bitly_token = 'Bearer %s' % os.environ.get("BITLY_GENERIC_ACCESS_TOKEN")
    print(bitly_token)
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
