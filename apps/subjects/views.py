from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subject, Test, Variant, Question
from .serializers import (
    SubjectSerializer,
    TestSerializer,
    VariantSerializer,
    QuestionSerializer,
    PromptSerializer,
)
from common.utils.question_ai import (
    ai_response,
    translate_text,
    detect_language_with_googletrans,
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


class AIResponseView(APIView):
    @swagger_auto_schema(
        request_body=PromptSerializer,
        responses={
            200: openapi.Response(
                "Response Example", example={"response": "AI Response Example"}
            )
        },
    )
    def post(self, request):
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data.get("prompt")
            detected_language = detect_language_with_googletrans(prompt)
            if detected_language == "uz":
                prompt = translate_text(prompt, "uz", "en")
                ai_answer = ai_response(prompt)
                return Response(
                    {"response": translate_text(ai_answer, "en", "uz")},
                    status=status.HTTP_200_OK,
                )
            else:
                prompt = translate_text(prompt, detected_language, "en")
                ai_answer = ai_response(prompt)
                return Response(
                    {"response": translate_text(ai_answer, "en", "uz")},
                    status=status.HTTP_200_OK,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
