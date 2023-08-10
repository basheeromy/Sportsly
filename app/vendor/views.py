"""
Views to manage Vendor related business logics.
"""

from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from product.models import Product
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from drf_spectacular.utils import extend_schema
from product.serializers import ProductSerializer
from vendor.serializers import (
    VendorSerializer
)



class CreateVendorView(CreateAPIView):
    """Create a new vendor."""
    serializer_class = VendorSerializer


class ListProductView(ListAPIView):
    serializer_class = ProductSerializer
    def get(self, request, format=None):
        product = Product.objects.filter(seller=request.user)
        serializer = ProductSerializer(product, many=True)

        return Response(serializer.data)

class CreateProductView(CreateAPIView):
    """Create a new Product"""
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]



class UpdateProductView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()

    def get_object(self):
        """Over ride get_object method"""
        try:
            id = self.request.data['id']
            instance = Product.objects.get(id=id)
            return instance
        except:
            return False
        
    def update(self, request, *args, **kwargs):
        """Update a product."""
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
                {"message": "product updated successfully",
                 "data":serializer.data}
            )
        else:
            return Response({"message": "failed"})

