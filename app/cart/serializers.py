"""
Serializers to manange cart items and wishlist.
"""
from rest_framework import serializers

from .models import (
    CartItem
)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'quantity',
            'user'
        ]
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        """Add new item to cart"""
        user = (self.context['request']).user
        cart = CartItem.objects.filter(user=user)
        cartitem = cart.filter(product=validated_data['product']).first()
        if cartitem:
            cartitem.quantity += validated_data['quantity']
            cartitem.save()
            return cartitem
        else:
            cartitem = CartItem(
                product = validated_data['product'],
                quantity = validated_data['quantity'],
                user = user,
            )
            cartitem.save()
            return cartitem



class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'quantity'
        ]
