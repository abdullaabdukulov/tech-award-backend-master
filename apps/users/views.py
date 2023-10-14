from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import (
    StudentRegistrationSerializer,
    LoginSerializer,
    StudentProfileSerializer,
)
from common.utils.custom_response_decorator import custom_response
from .response_schema import (
    STUDENT_REGISTER_REQUEST_BODY_SCHEMA,
    STUDENT_REGISTER_RESPONSE_SCHEMA_201,
    RESPONSE_SCHEMA_400,
    RESPONSE_SCHEMA_DEFAULT,
    login_schema,
    STUDENT_PROFILE_RESPONSE,
)


@custom_response
class StudentRegistrationView(APIView):
    @swagger_auto_schema(
        request_body=STUDENT_REGISTER_REQUEST_BODY_SCHEMA,
        responses={
            201: STUDENT_REGISTER_RESPONSE_SCHEMA_201,
            400: RESPONSE_SCHEMA_400,
            "default": RESPONSE_SCHEMA_DEFAULT,
        },
    )
    def post(self, request, format=None):
        serializer = StudentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @custom_response
class StudentLoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(**login_schema)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response(data, status=200)


@custom_response
class StudentRefreshTokenView(TokenRefreshView):
    """
    This view refreshes an access token by providing a valid refresh token.
    """

    pass


@custom_response
class StudentProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses=STUDENT_PROFILE_RESPONSE,
        operation_summary="Get information about the current authenticated user",
    )
    def get_object(self):
        return self.request.user
