# Generated by Django 4.2.6 on 2023-10-13 11:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "guid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=100, null=True, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=100, null=True, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=12,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="WRONG_PHONE_NUMBER",
                                message="Phone number must begin with 998 and contain only 12 numbers",
                                regex="^998\\d{9}$",
                            )
                        ],
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_image/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=(
                                    "jpeg",
                                    "jpg",
                                    "png",
                                    "heic",
                                    "heif",
                                ),
                                code="WRONG_IMAGE",
                                message="Wrong format uploaded image. Format must be: jpeg, jpg, png, heic or heif",
                            )
                        ],
                    ),
                ),
                ("address", models.TextField()),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("admin", "Admin"),
                            ("manager", "Manager"),
                            ("school_owner", "School Owner"),
                            ("student", "Student"),
                        ],
                        default="student",
                        max_length=20,
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="common.district",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="users",
                        to="common.region",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "db_table": "users",
            },
        ),
    ]
