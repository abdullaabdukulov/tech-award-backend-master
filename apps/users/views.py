from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import StudentRegistrationSerializer, LoginSerializer
from common.utils.custom_response_decorator import custom_response
from .response_schema import (
    STUDENT_REGISTER_REQUEST_BODY_SCHEMA,
    STUDENT_REGISTER_RESPONSE_SCHEMA_201,
    RESPONSE_SCHEMA_400,
    RESPONSE_SCHEMA_DEFAULT,
    login_schema,
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
class StudentLoginView(APIView):
    @swagger_auto_schema(**login_schema)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {
                    "access": str(RefreshToken.for_user(request.user).access_token),
                    "refresh": str(RefreshToken.for_user(request.user)),
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@custom_response
class StudentRefreshTokenView(TokenRefreshView):
    """
    This view refreshes an access token by providing a valid refresh token.
    """

    pass
