from django.urls import path

from .views import DistrictsAPIView, RegionsAPIView

urlpatterns = [
    path("regions/", RegionsAPIView.as_view(), name="regions"),
    path("districts/", DistrictsAPIView.as_view(), name="districts"),
]
