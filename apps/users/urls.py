from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from .views import StudentRegistrationView, StudentRefreshTokenView, StudentLoginView

urlpatterns = [
    path("register/", StudentRegistrationView.as_view(), name="student-registration"),
    path("login/", StudentLoginView.as_view(), name="student-login"),
    path(
        "token/refresh/",
        StudentRefreshTokenView.as_view(),
        name="student-refresh-token",
    ),
    path("token/verify/", TokenVerifyView.as_view(), name="student-token_verify"),
]
