from django.urls import path

from places.views import PlaceSearchView, CategoryListView, RegionListView

urlpatterns = [
    path('/search', PlaceSearchView.as_view()),
    path('/category', CategoryListView.as_view()),
    path('/region', RegionListView.as_view())
]
