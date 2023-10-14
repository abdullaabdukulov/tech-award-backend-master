from rest_framework import serializers
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
