"""Serializers to manage orders."""

from rest_framework import serializers
from order.models import (
    Order,
    OrderItem
)
from product.models import Product_item
from user.models import (
    Address,
    BillingAddress
)


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
    billing_address = serializers.PrimaryKeyRelatedField(
        queryset=BillingAddress.objects.all()
    )
    payment_mode = serializers.ChoiceField(
        choices=Order.PAYMENT_MODES
    )


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer to manage Order Items"""
    id = serializers.ModelField(
        model_field=OrderItem()._meta.get_field('id'))
    class Meta:

        model = OrderItem
        fields = [
            'id',
            'order',
            'seller',
            'product',
            'quantity',
            'price',
            'is_delete'

        ]


class OrderSerializer(serializers.ModelSerializer):
    """Serializer to manage order"""

    orderitem_set = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'orderitem_set',
            'id',
            'user',
            'shipping_address',
            'billing_address',
            'price',
            'order_status',
            'payment_mode',
            'payment_status'
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'price': {'read_only': True},
            'payment_status': {'read_only': True},
        }

    def update(self, instance, validated_data):

        instance.shipping_address = validated_data.get(
            'shipping_address',
            instance.shipping_address
        )
        instance.billing_address = validated_data.get(
            'billing_address',
            instance.billing_address
        )
        instance.order_status = validated_data.get(
            'order_status',
            instance.order_status
        )
        instance.payment_mode = validated_data.get(
            'payment_mode',
            instance.payment_mode
        )

        orderitems = validated_data.pop('orderitem_set', [])
        for orderitem_data in orderitems:
            id = orderitem_data.get('id')
            status = orderitem_data.get('is_delete')
            item_instance = OrderItem.objects.get(id=id)
            if status != item_instance.is_delete:
                item_instance.is_delete = status
                item_instance.save()
                continue
            product_price = item_instance.product.price
            quntity = orderitem_data.get('quantity')
            if quntity != item_instance.quantity and quntity is not None:
                item_instance.quantity = orderitem_data.get(
                    'quantity',
                    item_instance.quantity
                )
                item_instance.price = product_price * item_instance.quantity
                item_instance.save()

        instance.save()
        return instance
