import jwt, requests

from django.http  import JsonResponse
from django.views import View
from django.conf  import settings

from users.models import User, SocialNetwork, Platform

class KakaoSigninView(View):
    def get(self, request):
        try:
            kakao_token = request.headers.get('Authorization')
            KAKAO_URL   = 'https://kapi.kakao.com/v2/user/me'
            headers     = {'Authorization': f'Bearer {kakao_token}'}
            response    = requests.get(KAKAO_URL, headers=headers, timeout=3)
            kakao_user  = response.json()

            kakao_id          = kakao_user['id']
            kakao_nickname    = kakao_user['kakao_account']['profile']['nickname']
            kakao_email       = kakao_user['kakao_account']['email']
            profile_image_url = kakao_user['kakao_account']['profile']['profile_image_url']

            kakao                 = SocialNetwork.objects.get(name='kakao').id
            platform, is_created  = Platform.objects.get_or_create(
                serial_number     = kakao_id,
                social_network_id = kakao
            )
            user, is_created      = User.objects.get_or_create(
                platform = platform,
                defaults = {
                    'platform'          : platform,
                    'nickname'          : kakao_nickname,
                    'email'             : kakao_email,
                    'profile_image_url' : profile_image_url,
                }
            )

            access_token = jwt.encode({'id': user.id}, settings.SECRET_KEY, settings.ALGORITHM)

            if is_created:
                return JsonResponse({'message' : 'ACCOUNT_CREATED', 'access_token': access_token}, status=201)
            else:
                return JsonResponse({'message' : 'SIGN_IN_SUCCESS', 'access_token': access_token}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
