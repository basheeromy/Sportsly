
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from rest_framework.views import (APIView)
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from .models import (
    Product,
    Product_item,
    Banner,
    Category,
    Product_review
)
from .serializers import (
    ProductSerializer,
    ProductItemSerializer,
    BannerSerializer,
    CategorySerializer,
    ProductItemListSerializer,
    CategoryTreeSerializer,
    ProductTileSerializer,
    ProductItemDetailSerializer,
    productReviewListSerializer
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
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    #     # IsOwnerOrReadOnly

    # ]
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


class ProductItemDetailView(RetrieveAPIView):
    serializer_class = ProductItemDetailSerializer
    queryset = Product_item.objects.all()
    lookup_field = 'id'


class productReviewListView(ListAPIView):
    """Fetch all reviews related to a
    particular product.

    KWArgs:
        ListAPIView (product_id): product id
        is passed as url parameter. accessing
        product id from kwargs.
    """

    serializer_class = productReviewListSerializer

    def get_queryset(self):
        # customize queryset

        product_id = self.kwargs['product_id']
        return Product_review.objects.filter(product = product_id)


class similarProductListView(ListAPIView):
    """
    view to handle similar product listing API.
    """

    serializer_class = ProductTileSerializer


    def get_queryset(self):
        """
        """
        try:
            product_item_id = self.kwargs['product_id']
            product_item = Product_item.objects.get(id=product_item_id)
            category = product_item.name.category.all().values_list('id', flat=True)
            return Product_item.objects.filter(
                name__category__id__in=category
            ).exclude(name__id=product_item.name.id).order_by('name').distinct('name')

        except Product_item.DoesNotExist:
            return None
