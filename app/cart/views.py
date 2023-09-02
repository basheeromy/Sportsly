"""
Views to manage cart and wish list
"""

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
)
from permissions.custom_permissions import IsOwnerOrReadOnly

class AddCartItemView(ListCreateAPIView):
    """View to add items to cart and list cart items"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer
    queryset = CartItem.objects.filter()

    def get(self, request, format=None):
        product = CartItem.objects.filter(user=request.user)
        serializer = CartSerializer(product, many=True)

        return Response(serializer.data)
    

"""class UpdateCartView(UpdateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer
    queryset = CartItem.objects.filter()

    def get_object(self):


        try:
            id = self.request.data['id']
            instance = CartItem.objects.get(id=id)
            return instance
        except:
            return False

    def update(self, request, *args, **kwargs):


        instance = self.get_object()
        if instance is False:
            return Response({'message': 'Id not provided or wrong id',
                             'status':HTTP_400_BAD_REQUEST
                            }, 400)

        data = request.data
        serializer = self.get_serializer(instance, data, partial=True )
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {"message": "cart item updated successfully",
                 "data":serializer.data}
            )
        else:
            return Response({"message": "failed"})"""


class UpdateDeleteCartItem(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly

    ]
    queryset = CartItem.objects.all()
    serializer_class = CartUpdateSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["id"])
        self.check_object_permissions(self.request, obj)
        return obj
