from django.test import TestCase, Client

from places.models import Place, PlaceMenu, Menu, Price, Category, Image, Region

class PlaceSearchViewTest(TestCase):
    def setUp(self):
        Menu.objects.bulk_create([
            Menu(id = 1, name = '까눌레'),
            Menu(id = 2, name = '아메리카노'),
            Menu(id = 3, name = '핸드드립'),
            Menu(id = 4, name = '흑돼지고기국수'),
            Menu(id = 5, name = '돔베고기'),
            Menu(id = 6, name = '흑돼지비빔국수'),
        ])
        Price.objects.bulk_create([
            Price(id = 6, price = '3000'),
            Price(id = 10, price = '5000'),
            Price(id = 12, price = '6000'),
            Price(id = 16, price = '8000'),
            Price(id = 56, price = '28000'),
        ])
        Category.objects.bulk_create([
            Category(id = 1, name = '한식'),
            Category(id = 5, name = '카페'),
        ])
        Region.objects.bulk_create([
            Region(id = 2, name = '애월_한림'),
            Region(id = 4, name = '성산_표선'),
        ])
        Place.objects.bulk_create([
            Place(
                id                           = 1,
                name                         = '토투가커피',
                address                      = '제주특별자치도 제주시 한림읍 귀덕9길 19',
                phone_number                 = '010-6886-6121',
                opening_hours                = '10:00 - 18:00, 연중무휴',
                description                  = '맞아, 까눌레는 이래야지! 라는 말이 절로 나오는 집!',
                maximum_number_of_subscriber = '0',
                latitude                     = '33.44283842',
                longitude                    = '126.289942',
                able_to_reserve              =  False,
                closed_temporarily           =  False,
                category_id                  = '5',
                region_id                    = '2',
            ),
            Place(
                id                           = 2,
                name                         = '꽃가람',
                address                      = '제주특별자치도 서귀포시 성산읍 고성동서로 73',
                phone_number                 = '064-783-3939',
                opening_hours                = '09:10 - 20:00, 매 주 목요일 휴무',
                description                  = '담백하고 깔끔한 고기국수를 맛볼 수 있는 곳!',
                maximum_number_of_subscriber = '6',
                latitude                     = '33.45089738',
                longitude                    = '126.9149578',
                able_to_reserve              =  True,
                closed_temporarily           =  False,
                category_id                  = '1',
                region_id                    = '4',
            )
        ])
        PlaceMenu.objects.bulk_create([
            PlaceMenu(menu_id = 1, place_id = 1, price_id = 6, is_signature = True),
            PlaceMenu(menu_id = 2, place_id = 1, price_id = 10, is_signature = True),
            PlaceMenu(menu_id = 3, place_id = 1, price_id = 12, is_signature = False),
            PlaceMenu(menu_id = 4, place_id = 2, price_id = 16, is_signature = True),
            PlaceMenu(menu_id = 5, place_id = 2, price_id = 56, is_signature = True),
            PlaceMenu(menu_id = 6, place_id = 2, price_id = 16, is_signature = False),
        ])
        Image.objects.bulk_create([
            Image(id = 1, image_url = 'https://mustgo.carmore.kr/data/file/matzip/977797506_dMG6qOYk_bbb37afa85c4c5bf67abe3e40aea39f356c852bf.jpeg', place_id  = 1),
            Image(id = 51, image_url = 'https://cdn.pixabay.com/photo/2015/07/12/14/26/coffee-842020__480.jpg', place_id  = 1),
            Image(id = 52, image_url = 'https://media.istockphoto.com/photos/traditional-cafe-picture-id1356951371?b=1&k=20&m=1356951371&s=170667a&w=0&h=OCoZRi_qJmIiUvMRt8qMxHVraRtklgte4QtfDbeFSgM=', place_id  = 1),
            Image(id = 53, image_url = 'https://cdn.pixabay.com/photo/2014/12/11/02/55/cereals-563796__480.jpg', place_id  = 1),
            Image(id = 54, image_url = 'https://images.unsplash.com/photo-1481391032119-d89fee407e44?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTR8fGZvb2RzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60', place_id  = 1),
            Image(id = 55, image_url = 'https://cdn.pixabay.com/photo/2017/07/28/14/29/macarons-2548827__480.jpg', place_id  = 1),
            Image(id = 2, image_url = 'https://mustgo.carmore.kr/data/file/matzip/977797506_TEPcAJMy_8808aea72589ba335d85f349ce8729bbb4144445.jpeg', place_id  = 2),
            Image(id = 56, image_url = 'https://media.istockphoto.com/photos/korean-bbq-picture-id503205965?b=1&k=20&m=503205965&s=170667a&w=0&h=ilozw4fmtVJRaW_J7i5DiGj2CldrECeoCAM-GmuCQlw=', place_id  = 2),
            Image(id = 57, image_url = 'https://media.istockphoto.com/photos/sharing-good-food-and-wine-with-friend-picture-id949081542?b=1&k=20&m=949081542&s=170667a&w=0&h=HCivTNySVjMQ6xQKVJUhh9Y0EOiHNN0seh_gaPthWWQ=', place_id  = 2),
            Image(id = 58, image_url = 'https://images.unsplash.com/photo-1590301157890-4810ed352733?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8a29yZWFuJTIwZm9vZHN8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60', place_id  = 2),
            Image(id = 59, image_url = 'https://images.unsplash.com/photo-1553163147-622ab57be1c7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8a29yZWFuJTIwZm9vZHN8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60', place_id  = 2),
            Image(id = 60, image_url = 'https://media.istockphoto.com/photos/korean-seafood-tofu-stew-picture-id157774918?b=1&k=20&m=157774918&s=170667a&w=0&h=nEyobW5LyAXhSWQlfIoVEwHgqDsVzYvibCFU2XRZKy0=', place_id  = 2),
        ])

    def tearDown(self):
        Menu.objects.all().delete()
        Price.objects.all().delete()
        Category.objects.all().delete()
        Region.objects.all().delete()
        Place.objects.all().delete()
        PlaceMenu.objects.all().delete()
        Image.objects.all().delete()

    def test_success_place_search_get(self):
        client = Client()

        response = client.get('/places/search?date=2022-02-07')

        self.assertEqual(response.json(),{
            "results": [
                {
                    "place_id": 1,
                    "place_name": "토투가커피",
                    "place_opening_hours": "10:00 - 18:00, 연중무휴",
                    "place_maximum_number_of_subscriber": 0,
                    "place_able_to_reserve": False,
                    "place_closed_temporarily": False,
                    "place_category": "카페",
                    "place_region": "애월_한림",
                    "place_image": "https://mustgo.carmore.kr/data/file/matzip/977797506_dMG6qOYk_bbb37afa85c4c5bf67abe3e40aea39f356c852bf.jpeg",
                    "menus": [
                        {
                            "id": 1,
                            "name": "까눌레",
                            "price": "3000",
                            "is_signature": True
                        },
                        {
                            "id": 2,
                            "name": "아메리카노",
                            "price": "5000",
                            "is_signature": True
                        },
                        {
                            "id": 3,
                            "name": "핸드드립",
                            "price": "6000",
                            "is_signature": False
                        }
                    ],
                    "menu_avg_price": "4666.6667",
                    "menu_min_price": "3000",
                    "menu_max_price": "6000"
                },
                {
                    "place_id": 2,
                    "place_name": "꽃가람",
                    "place_opening_hours": "09:10 - 20:00, 매 주 목요일 휴무",
                    "place_maximum_number_of_subscriber": 6,
                    "place_able_to_reserve": True,
                    "place_closed_temporarily": False,
                    "place_category": "한식",
                    "place_region": "성산_표선",
                    "place_image": "https://mustgo.carmore.kr/data/file/matzip/977797506_TEPcAJMy_8808aea72589ba335d85f349ce8729bbb4144445.jpeg",
                    "menus": [
                        {
                            "id": 4,
                            "name": "흑돼지고기국수",
                            "price": "8000",
                            "is_signature": True
                        },
                        {
                            "id": 5,
                            "name": "돔베고기",
                            "price": "28000",
                            "is_signature": True
                        },
                        {
                            "id": 6,
                            "name": "흑돼지비빔국수",
                            "price": "8000",
                            "is_signature": False
                        }
                    ],
                    "menu_avg_price": "14666.6667",
                    "menu_min_price": "8000",
                    "menu_max_price": "28000"
                }
            ],
            "date": "2022-02-07"
        })
        self.assertEqual(response.status_code, 200)

    def test_success_place_search_get_filtered_by_categories(self):
            client = Client()

            response = client.get('/places/search?date=2022-02-07&category=5')

            self.assertEqual(response.json(),{
                "results": [
                    {
                        "place_id": 1,
                        "place_name": "토투가커피",
                        "place_opening_hours": "10:00 - 18:00, 연중무휴",
                        "place_maximum_number_of_subscriber": 0,
                        "place_able_to_reserve": False,
                        "place_closed_temporarily": False,
                        "place_category": "카페",
                        "place_region": "애월_한림",
                        "place_image": "https://mustgo.carmore.kr/data/file/matzip/977797506_dMG6qOYk_bbb37afa85c4c5bf67abe3e40aea39f356c852bf.jpeg",
                        "menus": [
                            {
                                "id": 1,
                                "name": "까눌레",
                                "price": "3000",
                                "is_signature": True
                            },
                            {
                                "id": 2,
                                "name": "아메리카노",
                                "price": "5000",
                                "is_signature": True
                            },
                            {
                                "id": 3,
                                "name": "핸드드립",
                                "price": "6000",
                                "is_signature": False
                            }
                        ],
                        "menu_avg_price": "4666.6667",
                        "menu_min_price": "3000",
                        "menu_max_price": "6000"
                    }
                ],
                "date": "2022-02-07"
            })
            self.assertEqual(response.status_code, 200)

    def test_success_place_search_get_filtered_by_regions(self):
            client = Client()

            response = client.get('/places/search?date=2022-02-07&region=4')

            self.assertEqual(response.json(),{

                "results": [
                    {
                        "place_id": 2,
                        "place_name": "꽃가람",
                        "place_opening_hours": "09:10 - 20:00, 매 주 목요일 휴무",
                        "place_maximum_number_of_subscriber": 6,
                        "place_able_to_reserve": True,
                        "place_closed_temporarily": False,
                        "place_category": "한식",
                        "place_region": "성산_표선",
                        "place_image": "https://mustgo.carmore.kr/data/file/matzip/977797506_TEPcAJMy_8808aea72589ba335d85f349ce8729bbb4144445.jpeg",
                        "menus": [
                            {
                                "id": 4,
                                "name": "흑돼지고기국수",
                                "price": "8000",
                                "is_signature": True
                            },
                            {
                                "id": 5,
                                "name": "돔베고기",
                                "price": "28000",
                                "is_signature": True
                            },
                            {
                                "id": 6,
                                "name": "흑돼지비빔국수",
                                "price": "8000",
                                "is_signature": False
                            }
                        ],
                        "menu_avg_price": "14666.6667",
                        "menu_min_price": "8000",
                        "menu_max_price": "28000"
                    }
                ],
                "date": "2022-02-07"
            })
            self.assertEqual(response.status_code, 200)

    def test_success_place_detail_get(self):
            client = Client()

            response = client.get('/places/1')

            self.assertEqual(response.json(),{
                "results": {
                    "place_id": 1,
                        "place_name": "토투가커피",
                        "place_address": "제주특별자치도 제주시 한림읍 귀덕9길 19",
                        "place_opening_hours": "10:00 - 18:00, 연중무휴",
                        "place_description": "맞아, 까눌레는 이래야지! 라는 말이 절로 나오는 집!",
                        "place_maximum_number_of_subscriber": 0,
                        "place_latitude": "33.44283842",
                        "place_longitude": "126.28994200",
                        "place_able_to_reserve": False,
                        "place_closed_temporarily": False,
                        "place_category": "카페",
                        "place_region": "애월_한림",
                        "place_images": [
                            {
                                "id": 1,
                                "url": "https://mustgo.carmore.kr/data/file/matzip/977797506_dMG6qOYk_bbb37afa85c4c5bf67abe3e40aea39f356c852bf.jpeg"
                            },
                            {
                                "id": 51,
                                "url": "https://cdn.pixabay.com/photo/2015/07/12/14/26/coffee-842020__480.jpg"
                            },
                            {
                                "id": 52,
                                "url": "https://media.istockphoto.com/photos/traditional-cafe-picture-id1356951371?b=1&k=20&m=1356951371&s=170667a&w=0&h=OCoZRi_qJmIiUvMRt8qMxHVraRtklgte4QtfDbeFSgM="
                            },
                            {
                                "id": 53,
                                "url": "https://cdn.pixabay.com/photo/2014/12/11/02/55/cereals-563796__480.jpg"
                            },
                            {
                                "id": 54,
                                "url": "https://images.unsplash.com/photo-1481391032119-d89fee407e44?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTR8fGZvb2RzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
                            },
                            {
                                "id": 55,
                                "url": "https://cdn.pixabay.com/photo/2017/07/28/14/29/macarons-2548827__480.jpg"
                            }
                        ],
                        "menus": [
                            {
                                "id": 1,
                                "name": "까눌레",
                                "price": "3000",
                                "is_signature": True
                            },
                            {
                                "id": 2,
                                "name": "아메리카노",
                                "price": "5000",
                                "is_signature": True
                            },
                            {
                                "id": 3,
                                "name": "핸드드립",
                                "price": "6000",
                                "is_signature": False
                            }
                        ]
                }
            })
            self.assertEqual(response.status_code, 200)
