from django.urls import path

from places.views import PlaceSearchView

urlpatterns = [
    path('/search', PlaceSearchView.as_view())
]
