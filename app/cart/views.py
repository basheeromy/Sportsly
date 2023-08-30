"""
Views to manage cart and wish list
"""

from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

class AddCartItemView(ListCreateAPIView):
    """View to add items to cart and list cart items"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer

    def get(self, request, format=None):
        product = CartItem.objects.filter(user=request.user)
        serializer = CartSerializer(product, many=True)

        return Response(serializer.data)



