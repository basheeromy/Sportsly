"""
    Serializers to manage wish list.
"""

from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from product.serializers import ProductItemSerializer


from .models import *

class ProductItemRelatedField(serializers.PrimaryKeyRelatedField):
    """
        Custom serializer field to handle
        string representation and internal
        value insertion.
    """
    def to_representation(self, value):
        product_item = Product_item.objects.get(id=(str(value)))

        serializer = ProductItemSerializer(instance=product_item, context=self.context)
        return serializer.data

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(pk=data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Invalid product item.')


class WishListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    product_item = ProductItemRelatedField(
        queryset=Product_item.objects.all()
    )
    class Meta:
        model = WishList
        fields = [
            'id',
            'user',
            'product_item',
            'created_at'
        ]
        # extra_kwargs = {'user': {'read_only': True}}
