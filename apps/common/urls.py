from django.urls import path
from .views import chatbot

urlpatterns = [
    path("chatbot/", chatbot, name="chatbot"),
]
