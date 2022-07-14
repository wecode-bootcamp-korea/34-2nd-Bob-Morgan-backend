import json

from datetime import datetime

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from places.models       import Place
from reservations.models import Reservation, Timeline
from core.utils          import signin_decorator

class PlaceReservationView(View):
    @signin_decorator
    def post(self, request, place_id):
        try:
            data = json.loads(request.body)

            place                        = Place.objects.get(id=place_id)
            closed_temporarily           = place.closed_temporarily
            able_to_reserve              = place.able_to_reserve
            maximum_number_of_subscriber = int(place.maximum_number_of_subscriber)
            reservation_date             = datetime.strptime(data['reservation_date'], '%Y-%m-%d')
            under_name                   = data['under_name']
            number_of_people             = int(data['number_of_people'])
            request_message              = data['request_message']
            reservation_time             = data['reservation_time']
            user_id                      = request.user.id

            timeline = Timeline.objects.get(time = reservation_time)

            if able_to_reserve == 0:
                return JsonResponse({'message' : 'PLACE_NOT_ABLE_TO_RESERVE'}, status = 400)

            if closed_temporarily == 1:
                return JsonResponse({'message' : 'CLOSED_TEMPORARILY'}, status = 400)

            if reservation_date < datetime.strptime((datetime.now().strftime('%Y-%m-%d')), '%Y-%m-%d'):
                return JsonResponse({'message' : 'DATE_NOT_AVAILABLE_FOR_RESERVATION'}, status = 400)

            if maximum_number_of_subscriber < number_of_people:
                return JsonResponse({'message' : 'REACHED_THE_RESERVATIONS_LIMIT'}, status = 400)

            if Reservation.objects.filter(Q(user_id = user_id) & Q(timeline = timeline) & Q(place_id = place.id)):
                return JsonResponse({'message' : 'YOU_ALREADY_BEEN_RESERVED'}, status = 400)

            Reservation.objects.create(
                reservation_date = reservation_date,
                under_name       = under_name,
                number_of_people = number_of_people,
                request          = request_message,
                place_id         = place_id,
                timeline         = timeline,
                user_id          = user_id,
            )

            return JsonResponse({'message' : 'RESERVATION_SUCCEESSFUL'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        except Timeline.DoesNotExist:
            return JsonResponse({'message' : 'INCORRECT TIMELINE'}, status = 400)
