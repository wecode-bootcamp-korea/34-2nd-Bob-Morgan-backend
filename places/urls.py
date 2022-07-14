from django.urls import path

from places.views import PlaceSearchView, CategoryListView, RegionListView, PlaceDetailView

urlpatterns = [
    path('/search', PlaceSearchView.as_view()),
    path('/region', RegionListView.as_view()),
    path('/category', CategoryListView.as_view()),
    path('/<int:place_id>', PlaceDetailView.as_view()),
]
