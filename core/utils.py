import requests

class KaKaoAPI:
    # def __init__(self, rest_api_key, redirect_url):
    #     self.rest_api_key = rest_api_key
    #     self.redirect_url = redirect_url

    def get_user_info(token):
        url     = 'https://kapi.kakao.com/v2/user/me'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers, timeout=3)

        return response.json()