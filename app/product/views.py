
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import (
    Product,
    Product_item
)
from .serializers import (
    ProductSerializer,
    ProductItemSerializer
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

        return Response(serializer.data)