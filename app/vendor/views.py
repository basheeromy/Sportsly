"""
Views to manage Vendor related business logics.
"""

from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from product.models import (
    Product,
    Product_item,
    Category,
    Size,
    Color,
    Product_Image
)
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from product.serializers import (
    ProductSerializer,
    ProductItemSerializer,
    ProductItemListSerializer,
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
    """
    Create a new vendor.
    """

    serializer_class = VendorSerializer


class ListCreateProductView(ListCreateAPIView):
    """
    List and create product.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()

    def get(self, request, format=None):
        product = Product.objects.filter(owner=request.user)
        serializer = ProductSerializer(product, many=True)

        return Response(serializer.data)


class UpdateDeleteProductView(RetrieveUpdateDestroyAPIView):
    """
    View to update and delete product.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        custom_permissions.IsSellerUser,
        custom_permissions.IsSellerOrReadOnly
    ]
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["id"])
        self.check_object_permissions(self.request, obj)

        return obj


class ListCreateProductItemView(ListCreateAPIView):
    """
    List and create product.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = ProductItemSerializer
    queryset = Product_item.objects.select_related(
            'name'
        ).filter()

    def get_serializer_class(self):
        # choose serializer class based on request method.

        if self.request.method == 'POST':
            return ProductItemSerializer
        return ProductItemListSerializer

    def get(self, request, format=None):
        product = Product_item.objects.select_related(
            'name'
        ).filter(name__owner=request.user)

        serializer = ProductItemListSerializer(product, many=True)

        return Response(serializer.data)


class UpdateDeleteProductItemView(RetrieveUpdateDestroyAPIView):
    """
    View to update and delete product item.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        custom_permissions.IsSellerUser
    ]
    queryset = Product_item.objects.select_related(
            'name'
        ).filter()
    serializer_class = ProductItemSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs["id"]
        )
        return obj


class ListCreateCategoryView(ListCreateAPIView):
    """
    List available categories and Create new category
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, format=None):
        serializer = CategorySerializer(
            self.get_queryset(),
            many=True
        )
        return Response(serializer.data)


class UpdateDeleteCategoryView(RetrieveUpdateDestroyAPIView):
    """
    View to update and delete Category.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        custom_permissions.IsSellerUser,
        custom_permissions.IsSellerOrReadOnly
    ]
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs["id"]
        )
        self.check_object_permissions(self.request, obj)

        return obj


class ListCreateSizeView(ListCreateAPIView):
    """
    List and create size.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = SizeSerializer
    queryset = Size.objects.all()

    def get(self, request, format=None):
        serializer = SizeSerializer(
            self.get_queryset(),
            many=True
        )
        return Response(serializer.data)


class UpdateDeleteSizeView(RetrieveUpdateDestroyAPIView):
    """
    View to update and delete Size.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        custom_permissions.IsSellerUser,
        custom_permissions.IsSellerOrReadOnly
    ]
    queryset = Size.objects.filter()
    serializer_class = SizeSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs["id"]
        )
        self.check_object_permissions(self.request, obj)

        return obj


class ListCreateColorView(ListCreateAPIView):
    """
    List and create color.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = ColorSerializer
    queryset = Color.objects.all()

    def get(self, request, format=None):
        serializer = ColorSerializer(
            self.get_queryset(),
            many=True
        )
        return Response(serializer.data)


class UpdateDeleteColorView(RetrieveUpdateDestroyAPIView):
    """
    View to update and delete color.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        custom_permissions.IsSellerUser,
        custom_permissions.IsSellerOrReadOnly
    ]
    queryset = Color.objects.filter()
    serializer_class = ColorSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs["id"]
        )
        self.check_object_permissions(self.request, obj)

        return obj


class ListCreateImageView(ListCreateAPIView):
    """
    View to list and upload images.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [custom_permissions.IsSellerUser]
    serializer_class = ImageSerializer
    queryset = Product_Image.objects.all()

    def get(self, request, format=None):
        serializer = ImageSerializer(
            self.get_queryset(),
            many=True
        )
        return Response(serializer.data)


class UpdateDeleteImageView(RetrieveUpdateDestroyAPIView):
    """
    View to delete and update image.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        custom_permissions.IsSellerUser,
        custom_permissions.IsSellerOrReadOnly
    ]
    queryset = Product_Image.objects.filter()
    serializer_class = ImageSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs["id"]
        )
        self.check_object_permissions(
            self.request,
            obj
        )

        return obj
