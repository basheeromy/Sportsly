"""
Views to manage Vendor related business logics.
"""

from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from vendor.serializers import VendorSerializer



class CreateVendorView(CreateAPIView):
    """Create a new vendor."""
    serializer_class = VendorSerializer
