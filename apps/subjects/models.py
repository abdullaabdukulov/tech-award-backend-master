from django.db import models
from common.models import BaseModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


User = get_user_model()


class Subject(BaseModel):
    class GroupChoices(models.TextChoices):
        EIGHT_GROUP = "eight_group"
        NINE_GROUP = "nine_group"
        TEN_GROUP = "ten_group"
        ELEVEN_GROUP = "eleven_group"

    group = models.CharField(
        max_length=255,
        choices=GroupChoices.choices,
    )
    title = models.CharField(max_length=255)

    class Meta:
        db_table = "subject"
        verbose_name = _("subject")
        verbose_name_plural = _("subjects")


class Test(BaseModel):
    class TypeChoices(models.TextChoices):
        WEEK = "week"
        QUARTER = "quarter"

    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, related_name="tests"
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    type = models.CharField(max_length=255, choices=TypeChoices.choices)

    class Meta:
        db_table = "test"


class Variant(BaseModel):
    title = models.CharField(max_length=255)


class Question(BaseModel):
    title = models.CharField(max_length=255)
    question = models.ForeignKey(
        Test, on_delete=models.SET_NULL, null=True, related_name="subjects_questions"
    )
    correct_option = models.ForeignKey(
        Variant, on_delete=models.SET_NULL, null=True, related_name="variants"
    )

    class Meta:
        db_table = "questions"
