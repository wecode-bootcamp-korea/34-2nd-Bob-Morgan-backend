import jwt, requests

from django.conf import settings
from django.http import JsonResponse

from users.models import User

class KakaoAPI:
    def get_user_info(token):
        url      = 'https://kapi.kakao.com/v2/user/me'
        headers  = {'Authorization' : f'Bearer {token}'}
        response = requests.get(url, headers = headers, timeout = 3)

        return response.json()

def signin_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token        = request.headers.get('Authorization', None)
            payload      = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
            request.user = User.objects.get(id = payload['id'])

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status = 400)

        except jwt.exceptions.InvalidTokenError:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status = 400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'USER_DOES_NOT_EXIST'}, status = 400)

        return func(self, request, *args, **kwargs)

    return wrapper
