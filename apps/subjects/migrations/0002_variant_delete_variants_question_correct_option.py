# Generated by Django 4.2.6 on 2023-10-14 06:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("subjects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Variant",
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
                ("published_at", models.DateTimeField(auto_now_add=True)),
                ("updated_time", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="Variants",
        ),
        migrations.AddField(
            model_name="question",
            name="correct_option",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="variants",
                to="subjects.variant",
            ),
        ),
    ]