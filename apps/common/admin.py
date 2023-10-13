from django.contrib import admin

from .models import Region, District


@admin.register(Region)
class RegionModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name_uz", "name_ru", "guid")
    search_fields = ("name_uz", "name_ru")


@admin.register(District)
class DistrictModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name_uz", "name_ru", "region", "guid")
    search_fields = ("name_uz", "name_ru")
    list_filter = ("region",)
