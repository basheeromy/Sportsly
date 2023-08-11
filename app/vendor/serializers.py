"""Serializers for Vendor views."""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class VendorSerializer(serializers.ModelSerializer):
    """Serializer to create vendor"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'mobile', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a vendor user."""

        return get_user_model().objects.create_vendor_user(**validated_data)
