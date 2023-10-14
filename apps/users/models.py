import random
import uuid

from apps.common.validators import image_common_extensions, validate_phone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.cache import cache
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from .managers import UserManager
from common.models import Region, District


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "admin"
        STUDENT = "student"

        @classmethod
        def admins(cls):
            return [cls.ADMIN.value]

    guid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, db_index=True
    )
    first_name = models.CharField(
        max_length=100, null=True, verbose_name=_("first name")
    )
    last_name = models.CharField(max_length=100, null=True, verbose_name=_("last name"))

    email = models.EmailField(_("email address"), unique=True, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    phone = models.CharField(
        max_length=12,
        unique=True,
        validators=[validate_phone],
        null=True,
    )
    image = models.ImageField(
        upload_to="profile_image/",
        validators=[image_common_extensions],
        null=True,
        blank=True,
    )
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, related_name="users"
    )
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True, related_name="users"
    )
    address = models.TextField(null=True, blank=True)
    role = models.CharField(
        choices=Role.choices,
        max_length=20,
        default=Role.STUDENT,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.email is not None:
            return self.email
        if self.first_name is not None:
            return f"{self.first_name} {self.last_name}"
        if self.phone is not None:
            return self.phone

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        # indexes = [
        #     GinIndex(
        #         fields=["username"],
        #         name="username_index",
        #         opclasses=["gin_trgm_ops"],
        #     ),
        #     GinIndex(
        #         fields=["phone"],
        #         name="phone_index",
        #         opclasses=["gin_trgm_ops"],
        #     ),
        # ]

    # @property
    # def region_name(self):
    #     return self.region.name

    # @property
    # def district_name(self):
    #     return self.district.name

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}

    @staticmethod
    def generate_code():
        return random.randint(100000, 999999)

    @staticmethod
    def add_to_cache(key, value, ttl=120):
        """If the entered key is already taken,
        then returns False
        """
        return cache.add(f"{key}", value, timeout=ttl)

    @staticmethod
    def set_to_cache(key, value, ttl=120):
        """If the entered key is already taken,
        then set the new value and time
        """
        return cache.set(f"{key}", value, timeout=ttl)

    @staticmethod
    def clear_cache(cache_key):
        cache.delete(key=cache_key)
