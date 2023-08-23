"""
Views to manage Vendor related business logics.
"""

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from product.models import (
    Product,
    Category,
    Size,
    Color,
    Product_Image
)
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListCreateAPIView,
)
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
)

from product.serializers import (
    ProductSerializer,
    CategorySerializer,
    SizeSerializer,
    ColorSerializer,
    ImageSerializer
)
from vendor.serializers import (
    VendorSerializer
)

from permissions import custom_permissions


class CreateVendorView(CreateAPIView):
    """Create a new vendor."""
    serializer_class = VendorSerializer


class ListCreateProductView(ListCreateAPIView):
    """List and create product."""

    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        product = Product.objects.filter(seller=request.user)
        serializer = ProductSerializer(product, many=True)

        return Response(serializer.data)


class UpdateProductView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
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

    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = CategorySerializer

    def get(self, request, format=None):
        category_list = Category.objects.all()
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)


class UpdateCategoryView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
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

                            }, status = HTTP_400_BAD_REQUEST)

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
    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = SizeSerializer

    def get(self, request, format=None):
        category_list = Size.objects.all()
        serializer = SizeSerializer(category_list, many=True)
        return Response(serializer.data)


class UpdateSizeView(UpdateAPIView):
    """Update Size."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
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


class ListCreateColorView(ListCreateAPIView):
    """List and create color."""

    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = ColorSerializer

    def get(self, request, format=None):
        color_list = Color.objects.all()
        serializer = ColorSerializer(color_list, many=True)
        return Response(serializer.data)


class UpdateColorView(UpdateAPIView):
    """Update Color."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = ColorSerializer
    queryset = Color.objects.filter()

    def get_object(self):
        """Over ride get_object method"""

        try:
            id = self.request.data['id']
            instance = Color.objects.get(id=id)
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
                {"message": "Color updated successfully",
                 "data":serializer.data}
            )
        else:
            return Response({"message": "failed"})


class ListCreateImageView(ListCreateAPIView):
    """
    View to list and upload images.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = ImageSerializer
    queryset = Product_Image.objects.all()

    def get(self, request, format=None):
        color_list = Product_Image.objects.all()
        serializer = ImageSerializer(color_list, many=True)
        return Response(serializer.data)