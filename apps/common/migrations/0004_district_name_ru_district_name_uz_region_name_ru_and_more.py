# Generated by Django 4.2.6 on 2023-10-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0003_district_created_time_district_updated_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="district",
            name="name_ru",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="district",
            name="name_uz",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="region",
            name="name_ru",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="region",
            name="name_uz",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
