
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema

class ProductListView(ListAPIView):

    @extend_schema(request=ProductSerializer, responses=None)
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)