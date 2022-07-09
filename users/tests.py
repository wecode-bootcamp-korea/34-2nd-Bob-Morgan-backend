import jwt

from django.test   import Client, TestCase
from django.conf   import settings
from unittest.mock import patch, MagicMock

from users.models import Platform, User, SocialNetwork

class KakaoSigninTest(TestCase):
    def setUp(self):
        SocialNetwork.objects.create(
            id   = 1,
            name = 'kakao',
        )
        Platform.objects.create(
            id                = 123456,
            serial_number     = 987654,
            social_network_id = SocialNetwork.objects.get(name='kakao').id,
        )
        User.objects.create(
            id          = 5,
            email       = 'test@kakao.com',
            nickname    = 'test',
            platform_id = Platform.objects.get(id=123456).id,
        )

    def tearDown(self):
        SocialNetwork.objects.all().delete()
        Platform.objects.all().delete()
        User.objects.all().delete()

    @patch('users.views.requests')
    def test_success_kakao_signup(self, mocked_requests):
        client = Client()
        class MockedResponse:
            def json(self):
                return {
                    'id': 11111111,
                    'connected_at' : '2022-07-07T04:35:56Z',
                    'properties'   : {
                        'nickname'       : 'signup',
                        'profile_image'  : 'http://k.kakaocdn.net/dn/bxmEfD/btryJYaBk0R/oPpMxh2NK73LSYT98Xl1Vk/img_640x640.jpg',
                        'thumbnail_image': 'http://k.kakaocdn.net/dn/bxmEfD/btryJYaBk0R/oPpMxh2NK73LSYT98Xl1Vk/img_110x110.jpg'},
                    'kakao_account': {
                        'profile_nickname_needs_agreement': False,
                        'profile_image_needs_agreement': False,
                        'profile': {
                            'nickname': 'signup',
                            'thumbnail_image_url': 'http://k.kakaocdn.net/dn/bxmEfD/btryJYaBk0R/oPpMxh2NK73LSYT98Xl1Vk/img_110x110.jpg',
                            'profile_image_url': 'http://k.kakaocdn.net/dn/bxmEfD/btryJYaBk0R/oPpMxh2NK73LSYT98Xl1Vk/img_640x640.jpg',
                            'is_default_image': False
                        },
                        'has_email': True,
                        'email_needs_agreement': False,
                        'is_email_valid': True,
                        'is_email_verified': True,
                        'email': 'kakao-signup@kakao.com'
                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization': 'mocked_access_token'}
        response            = client.get('/users/signin/kakao', **headers)
        access_token        = jwt.encode({'id': User.objects.latest('id').id}, settings.SECRET_KEY, settings.ALGORITHM)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),{
                'message'      : 'ACCOUNT_CREATED',
                'access_token' : access_token
            }
        )

    @patch('users.views.requests')
    def test_success_kakao_signin(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    'id': 987654,
                    'connected_at' : '2022-07-07T04:35:56Z',
                    'properties'   : {
                        'nickname'       : 'test',
                        'profile_image'  : 'http://k.kakaocdn.net/dn/bxmEfD/btryJYaBk0R/oPpMxh2NK73LSYT98Xl1Vk/img_640x640.jpg',
                        'thumbnail_image': 'http://k.kakaocdn.net/dn/bxmEfD/btryJYaBk0R/oPpMxh2NK73LSYT98Xl1Vk/img_110x110.jpg'},
                    'kakao_account': {
                        'profile_nickname_needs_agreement': False,
                        'profile_image_needs_agreement': False,
                        'profile': {
                            'nickname': 'test',
                            'thumbnail_image_url': 'http://k.kakaocdn.net/dn/bxmEfD/btryJYaBk0R/oPpMxh2NK73LSYT98Xl1Vk/img_110x110.jpg',
                            'profile_image_url': 'http://k.kakaocdn.net/dn/bxmEfD/btryJYaBk0R/oPpMxh2NK73LSYT98Xl1Vk/img_640x640.jpg',
                            'is_default_image': False
                        },
                        'has_email': True,
                        'email_needs_agreement': False,
                        'is_email_valid': True,
                        'is_email_verified': True,
                        'email': 'test@kakao.com'
                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization': 'mocked_access_token'}
        response            = client.get('/users/signin/kakao', **headers)
        access_token        = jwt.encode({'id': User.objects.latest('id').id}, settings.SECRET_KEY, settings.ALGORITHM)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),{
                'message'      : 'SIGN_IN_SUCCESS',
                'access_token' : access_token
            }
        )
