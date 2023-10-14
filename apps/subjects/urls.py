from django.urls import path
from .views import (
    SubjectListCreateView,
    SubjectDetailView,
    TestListCreateView,
    TestDetailView,
    VariantListCreateView,
    VariantDetailView,
    QuestionListCreateView,
    QuestionDetailView,
)

urlpatterns = [
    path("subjects/", SubjectListCreateView.as_view(), name="subject-list-create"),
    path("subjects/<int:pk>/", SubjectDetailView.as_view(), name="subject-detail"),
    path("tests/", TestListCreateView.as_view(), name="test-list-create"),
    path("tests/<int:pk>/", TestDetailView.as_view(), name="test-detail"),
    path("variants/", VariantListCreateView.as_view(), name="variant-list-create"),
    path("variants/<int:pk>/", VariantDetailView.as_view(), name="variant-detail"),
    path("questions/", QuestionListCreateView.as_view(), name="question-list-create"),
    path("questions/<int:pk>/", QuestionDetailView.as_view(), name="question-detail"),
]
