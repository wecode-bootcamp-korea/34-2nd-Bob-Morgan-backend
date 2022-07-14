from django.urls import path

from reservations.views import PlaceReservationView

urlpatterns = [
    path('/<int:place_id>', PlaceReservationView.as_view())
]
