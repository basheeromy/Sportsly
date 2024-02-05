
from rest_framework.generics import (
    ListAPIView
)
from rest_framework.response import Response
from rest_framework import permissions
from .models import (
    Product,
    Product_item,
    Banner,
    Category
)
from .serializers import (
    ProductSerializer,
    ProductItemSerializer,
    BannerSerializer,
    CategorySerializer
)
from drf_spectacular.utils import extend_schema

class ProductListView(ListAPIView):

    @extend_schema(request=ProductSerializer, responses=None)
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductItemListView(ListAPIView):

    @extend_schema(request=ProductItemSerializer, responses=None)
    def get(self, request, format=None):
        products = Product_item.objects.all()
        serializer = ProductItemSerializer(products, many=True)
        permission_classes = permissions.IsAuthenticatedOrReadOnly

        return Response(serializer.data)

class ListBanners(ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()

class TopLevelCategoriesAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()