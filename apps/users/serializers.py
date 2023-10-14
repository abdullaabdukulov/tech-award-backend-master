from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    def validate_email(self, value):
        if "@example.com" not in value:
            raise serializers.ValidationError("Email must be from example.com domain.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]

        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return {
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            }
        else:
            raise serializers.ValidationError("Invalid phone number or password")


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "image",
            "region",
            "district",
            "address",
        )
