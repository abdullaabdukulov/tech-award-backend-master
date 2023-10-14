from django.contrib import admin
from .models import Subject, Test, Variant, Question


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "group", "get_created_at")

    def get_created_at(self, obj):
        return obj.created_at

    get_created_at.short_description = "Created At"


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("subject", "start_date", "end_date", "type")


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ("title", "get_created_at")

    def get_created_at(self, obj):
        return obj.created_at

    get_created_at.short_description = "Created At"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "get_subject", "correct_option")

    def get_subject(self, obj):
        return obj.subject.title

    get_subject.short_description = "Subject"
