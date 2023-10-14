from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Import your User model here


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "guid",
        "phone",
        "email",
        "is_active",
        "role",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "role")
    search_fields = ("phone", "email", "guid")
    ordering = ("id",)

    fieldsets = (
        (None, {"fields": ("email", "password", "role")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "address",
                    "phone",
                    "image",
                    "region",
                    "district",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_staff", "is_superuser"),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "role"),
            },
        ),
    )
