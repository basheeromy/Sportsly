"""Serializers for user API views."""

from django.contrib.auth import (get_user_model)

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'mobile', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Handle updating user."""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class GenerateTokenSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data['email']
        password = data['password']
        if not email:
            raise serializers.ValidationError("Email is required.")
        elif not password:
            raise serializers.ValidationError("Password is required.")

        user = get_user_model().objects.filter(email__iexact=email)

        if not user.exists():
            raise serializers.ValidationError("User not found! Please register.")
        user = user.first()
        if user.check_password(password) == False:
            raise serializers.ValidationError("Incorrect Password.")
        if user.is_active == False:
            raise serializers.ValidationError(
                "user not activated."
            )

        return user


class GenerateOtpSerializer(serializers.Serializer):
    """Check mobile number valid or not"""

    mobile = serializers.CharField()

    def validate_mobile(self, mobile):
        """Check the mobile and user exist."""
        if not mobile:
            raise serializers.ValidationError("Phone number is required.")

        user = get_user_model().objects.filter(mobile__iexact=mobile)

        if not user.exists():
            raise serializers.ValidationError(
                "User not found! Please register."
            )



        return mobile


class ValidateOtpSerializer(serializers.Serializer):
    """Check mobile number and otp."""

    mobile = serializers.CharField()
    otp = serializers.CharField()

    def validate_mobile(self, mobile):
        """Check user and otp exists."""
        user = get_user_model().objects.filter(mobile__iexact=mobile)
        if not user.exists():
            raise serializers.ValidationError(
                "User not found! Please register."
            )

        return user
