import uuid

from django.db import models
from django.db.models.functions import Upper
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    guid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, db_index=True
    )
    published_at = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(models.Model):
    guid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, db_index=True
    )
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "regions"
        """Index for iexact lookups"""
        indexes = [
            models.Index(Upper("name_uz").desc(), name="region_name_uz_upper_index"),
            models.Index(Upper("name_ru").desc(), name="region_name_ru_upper_index"),
        ]


class District(models.Model):
    guid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, db_index=True
    )
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "districts"
        """Index for iexact lookup"""
        indexes = [
            models.Index(Upper("name_uz").desc(), name="district_name_uz_upper_index"),
            models.Index(Upper("name_ru").desc(), name="district_name_ru_upper_index"),
        ]


class StaticPage(models.Model):
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))
    content = models.TextField(verbose_name=_("Content"))

    def __str__(self) -> str:
        return str("".join(self.content.split()[:4])) + "..."
