"""Serializers to manage orders."""

from rest_framework import serializers
from order.models import (
    Order,
    OrderItem
)
from product.models import Product_item
from user.models import Address


class SpecialSerializer(serializers.Serializer):
    """
    Special serializer to help creation of order
    and order items with a single view.
    """
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product_item.objects.all(),
        many=True
    )
    quantity = serializers.DictField(
        child=serializers.IntegerField()
    )
    shipping_address = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all()
    )
    payment_mode = serializers.ChoiceField(choices=Order.PAYMENT_MODES)


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer to manage Order Items"""

    class Meta:
        model = OrderItem
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'order': {'read_only': True},
            'seller': {'read_only': True},
            'price': {'read_only': True}
        }


class OrderSerializer(serializers.ModelSerializer):
    """Serializer to manage order"""

    orderitem_set = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'price': {'read_only': True},
            'order_status': {'read_only': True},
            'payment_status': {'read_only': True},
        }
