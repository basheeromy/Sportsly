
from rest_framework.generics import (
    ListAPIView
)
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication
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
    CategorySerializer,
    ProductItemListSerializer,
    CategoryTreeSerializer,
    ProductTileSerializer
)

from .filters import ProductItemFilter
from drf_spectacular.utils import extend_schema
from django_filters import rest_framework as filters

from django.db.models import OuterRef, Subquery
from permissions.custom_permissions import IsOwnerOrReadOnly

class ProductListView(ListAPIView):

    @extend_schema(request=ProductSerializer, responses=None)
    def get(self, request, format=None):
        products = Product.objects.all()
        # print(products.get(id=5))
        print(Product.average_rating(products.get(id=5)))
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductItemListView(ListAPIView):

    queryset = Product_item.objects.all()
    serializer_class = ProductItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductItemFilter


class ProductTileListView(ListAPIView):
    """
        View to return all distinct product items

    """
    queryset = Product_item.objects.order_by('name').distinct('name')
    serializer_class = ProductTileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly

    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductItemFilter




class ListBanners(ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()

class ListCategoryTreeAPIView(ListAPIView):
    """
        List Category Tree.
    """
    serializer_class = CategoryTreeSerializer
    queryset = Category.objects.filter(parent__isnull=True)







    # def get(self, request, *args, **kwargs):

    #     categories = Category.objects.filter(parent__isnull=True)
    #     serializer = CategoryTreeSerializer(categories, many=True)

    #     return Response(serializer.data, status=status.HTTP_200_OK)



    # serializer_class = CategorySerializer
    # queryset = Category.objects.filter(parent__isnull=True)

    # def create_nested_category_dict(self, categories):
    #     nested_categories = {}
    #     for category in categories:
    #         nested_categories[category.id] = {
    #             'name': category.name,
    #             'children': self.create_nested_category_dict(category.get_children())
    #         }
    #     return nested_categories

    # nested_dict = self.create_nested_category_dict(categories)
        # print(nested_dict)
        # serializer = CategorySerializer(categories, many=True)
