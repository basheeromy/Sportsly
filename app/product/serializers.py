
from rest_framework import serializers
from .models import (
    Product,
    Product_item
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'is_active'
        ]

    def create(self, validated_data):
        """Create and return a new product"""
        user = (self.context['request']).user
        if user.is_seller == False:
            raise serializers.ValidationError("Register as a seller.")
        product = Product(
            name = validated_data['name'],
            description = validated_data['description'],
            seller = user,
            is_active = validated_data['is_active']
        )
        product.save()
        product.category.set(validated_data['category'])
        product.save()
        return product
