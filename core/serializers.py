from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


def username_validator(value):
    """
    Esto hace que solo se aplique esta validaction
    """
    if not any(char.isdigit() for char in value):
        raise serializers.ValidationError("Should be a least one digit")


# class UserSerializer(ModelSerializer):
#     # username = serializers.CharField(max_length=150, validators=[username_validator])
#
#     class Meta:
#         model = User
#         fields = "__all__"
#
#     def create(self, validated_data):
#         validated_data["password"] = make_password(validated_data["password"])
#         return User.objects.create(**validated_data)
#
#     def validate_password(self, value):
#         if value.islower():
#             raise serializers.ValidationError("Should be a least one upper case")
#         return value
#
#     def validate_username(self, username):
#         if not any(char.isdigit() for char in username):
#             raise serializers.ValidationError("Should be a least one digit")
#         return username
#

class CreateUserSerializer(ModelSerializer):
    # username = serializers.CharField(max_length=150, validators=[username_validator])

    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return User.objects.create(**validated_data)

    def validate_password(self, value):
        if value.islower():
            raise serializers.ValidationError("Should be a least one upper case")
        return value

    def validate_username(self, username):
        if not any(char.isdigit() for char in username):
            raise serializers.ValidationError("Should be a least one digit")
        return username


class UserSerializer(ModelSerializer):
    # username = serializers.CharField(max_length=150, validators=[username_validator])

    class Meta:
        model = User
        fields = ("username", "date_joined", "last_login")



