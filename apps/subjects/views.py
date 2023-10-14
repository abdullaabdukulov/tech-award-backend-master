from rest_framework import generics
from .models import Subject, Test, Variant, Question
from .serializers import (
    SubjectSerializer,
    TestSerializer,
    VariantSerializer,
    QuestionSerializer,
)


class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TestListCreateView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class VariantListCreateView(generics.ListCreateAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer


class VariantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
