"""Serializers for user API views."""

from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'mobile', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""

        return get_user_model().objects.create_user(**validated_data)


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
