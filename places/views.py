from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q, Avg, Min, Max

from places.models import Place, Category, Region

class CategoryListView(View):
    def get(self, request):
        result = [{
            'category_id'   : category.id,
            'category_name' : category.name
        } for category in Category.objects.all()]

        return JsonResponse({'category_list' : result}, status = 200)

class RegionListView(View):
    def get(self, request):
        result = [{
            'region_id' : region.id,
            'region_name' : region.name
        } for region in Region.objects.all()]

        return JsonResponse({'region_list' : result}, status = 200)

class PlaceSearchView(View):
    def get(self, request):
        try:
            date       = request.GET.get('date')
            regions    = request.GET.getlist('region')
            categories = request.GET.getlist('category')

            sort   = request.GET.get('sort')
            offset = int(request.GET.get('offset', 0))
            limit  = int(request.GET.get('limit', 20))

            q_region = Q()
            q_category = Q()

            if regions:
                q_region |= Q(region__id__in = regions)

            if categories:
                q_category |= Q(category__id__in = categories)

            sort_set = {
                'avg-price-ascending'  : 'avg_price',
                'avg-price-descending' : '-avg_price',
                'min-price-ascending'  : 'min_price',
                'max-price-descending' : '-max_price',
                'random'               : '?',
            }

            order_key = sort_set.get(sort, 'id')

            places = Place.objects.select_related('category', 'region').prefetch_related('placemenu_set__price', 'placemenu_set__menu', 'menus', 'image_set').annotate(
                min_price = Min('placemenu__price__price'),
                max_price = Max('placemenu__price__price'),
                avg_price = Avg('placemenu__price__price')
                ).filter(q_region & q_category).order_by(order_key)[offset : offset + limit]

            results = [{
                'place_id'                           : place.id,
                'place_name'                         : place.name,
                'place_opening_hours'                : place.opening_hours,
                'place_maximum_number_of_subscriber' : place.maximum_number_of_subscriber,
                'place_able_to_reserve'              : place.able_to_reserve,
                'place_closed_temporarily'           : place.closed_temporarily,
                'place_category'                     : place.category.name,
                'place_region'                       : place.region.name,
                'place_image'                        : place.image_set.all().first().image_url if place.image_set.all() else None,
                'menus' : [{
                    'id'           : placemenu.menu.id,
                    'name'         : placemenu.menu.name ,
                    'price'        : placemenu.price.price,
                    'is_signature' : placemenu.is_signature,
                } for placemenu in place.placemenu_set.all()],
                'menu_avg_price'                     : place.avg_price,
                'menu_min_price'                     : place.min_price,
                'menu_max_price'                     : place.max_price,
            } for place in places]

            return JsonResponse({'results' : results, 'date' : date}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
