"""
Views to manage Vendor related business logics.
"""

from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from product.models import (
    Product,
    Category,
    Size
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
)

from product.serializers import (
    ProductSerializer,
    CategorySerializer,
    SizeSerializer
)
from vendor.serializers import (
    VendorSerializer
)



class CreateVendorView(CreateAPIView):
    """Create a new vendor."""
    serializer_class = VendorSerializer


class ListCreateProductView(ListCreateAPIView):
    """List and create product."""

    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        product = Product.objects.filter(seller=request.user)
        serializer = ProductSerializer(product, many=True)

        return Response(serializer.data)


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

class ListCreateCategoryView(ListCreateAPIView):
    """List available categories and Create new category"""

    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        category_list = Category.objects.all()
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)

class UpdateCategoryView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()

    def get_object(self):

        """Over ride get_object method"""
        try:
            id = self.request.data['id']
            instance = Category.objects.get(id=id)
            return instance
        except:
            return False

    def update(self, request, *args, **kwargs):
        """Update a category."""

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
                {"message": "category updated successfully",
                 "data":serializer.data}
            )
        else:
            return Response({"message": "failed"})


class ListCreateSizeView(ListCreateAPIView):
    """List and create size."""

    serializer_class = SizeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        category_list = Size.objects.all()
        serializer = SizeSerializer(category_list, many=True)
        return Response(serializer.data)


class UpdateSizeView(UpdateAPIView):
    """Update Size."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SizeSerializer
    queryset = Size.objects.filter()

    def get_object(self):

        """Over ride get_object method"""
        try:
            id = self.request.data['id']
            instance = Size.objects.get(id=id)
            return instance
        except:
            return False


    def update(self, request, *args, **kwargs):
        """Update a category."""

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
                {"message": "Size updated successfully",
                 "data":serializer.data}
            )
        else:
            return Response({"message": "failed"})