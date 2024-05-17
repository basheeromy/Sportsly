"""
    Filters for product items
"""

from django_filters import rest_framework as filters
from .models import Product_item


class ProductItemFilter(filters.FilterSet):
    """
        This class helps to filter product items
        based on bellow defined criteria.
    """

    name = filters.CharFilter(
        field_name='name__name',
        lookup_expr='icontains'
    )
    size = filters.CharFilter(
        field_name='size__name',
        lookup_expr='icontains'
    )
    color = filters.CharFilter(
        field_name='color__name',
        lookup_expr='icontains'
    )
    min_price = filters.NumberFilter(
        field_name="price",
        lookup_expr='gte'
    )
    max_price = filters.NumberFilter(
        field_name="price",
        lookup_expr='lte'
    )

    discount = filters.NumberFilter(
        field_name="discount",
        lookup_expr="gte"
    )


    class Meta:
        model = Product_item
        fields = (
            'name',
            'color',
            'size',
            'discount'
        )