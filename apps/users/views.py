from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
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
class StudentLoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(**login_schema)
    def post(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = response.data.get("user")
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                },
                status=status.HTTP_200_OK,
            )
        return response


@custom_response
class StudentRefreshTokenView(TokenRefreshView):
    """
    This view refreshes an access token by providing a valid refresh token.
    """

    pass
