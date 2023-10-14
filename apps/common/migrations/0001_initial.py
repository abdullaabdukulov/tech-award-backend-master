# Generated by Django 4.2.6 on 2023-10-14 06:41

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StaticPage",
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
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
                ("content", models.TextField(verbose_name="Content")),
            ],
        ),
        migrations.CreateModel(
            name="Region",
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
                (
                    "guid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("name_uz", models.CharField(max_length=100, null=True)),
                ("name_ru", models.CharField(max_length=100, null=True)),
                ("created_time", models.DateTimeField()),
                ("updated_time", models.DateTimeField()),
            ],
            options={
                "db_table": "regions",
                "indexes": [
                    models.Index(
                        models.OrderBy(
                            django.db.models.functions.text.Upper("name_uz"),
                            descending=True,
                        ),
                        name="region_name_uz_upper_index",
                    ),
                    models.Index(
                        models.OrderBy(
                            django.db.models.functions.text.Upper("name_ru"),
                            descending=True,
                        ),
                        name="region_name_ru_upper_index",
                    ),
                ],
            },
        ),
        migrations.CreateModel(
            name="District",
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
                (
                    "guid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("name_uz", models.CharField(max_length=100, null=True)),
                ("name_ru", models.CharField(max_length=100, null=True)),
                ("created_time", models.DateTimeField()),
                ("updated_time", models.DateTimeField()),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="common.region"
                    ),
                ),
            ],
            options={
                "db_table": "districts",
                "indexes": [
                    models.Index(
                        models.OrderBy(
                            django.db.models.functions.text.Upper("name_uz"),
                            descending=True,
                        ),
                        name="district_name_uz_upper_index",
                    ),
                    models.Index(
                        models.OrderBy(
                            django.db.models.functions.text.Upper("name_ru"),
                            descending=True,
                        ),
                        name="district_name_ru_upper_index",
                    ),
                ],
            },
        ),
    ]
