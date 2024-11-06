"""
    Views to manage wish list.
"""
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, status
from permissions.custom_permissions import IsOwnerOrReadOnly

from .serializers import *


class ListCreateWishListView(ListCreateAPIView):
    """
    Manage wish list items
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WishListSerializer
    queryset = WishList.objects.filter()

    def get(self, request, format=None):
        product = WishList.objects.filter(user=request.user)
        serializer = WishListSerializer(product, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user
        product_item = request.data.get('product_item')

        if WishList.objects.filter(
            user=user,
            product_item=product_item
        ).exists():
            return Response(
                {'detail' : 'Item already wish listed by this user.' },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)