from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product_item
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema

class ProductListView(APIView):

    @extend_schema(request=ProductSerializer, responses=None)
    def get(self, request, format=None):
        products = Product_item.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)