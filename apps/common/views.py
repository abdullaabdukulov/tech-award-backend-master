from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter

from .models import District, Region
from .serializers import DistrictsSerializer, RegionsSerializer
from .utils.custom_response_decorator import custom_response


@custom_response
class RegionsAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegionsSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # pagination_class = ZonePagination
    search_fields = ("=name",)
    queryset = Region.objects.all()


@custom_response
class DistrictsAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = DistrictsSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # pagination_class = ZonePagination
    filterset_fields = ("region__guid",)
    search_fields = ("=name",)
    queryset = District.objects.all()
