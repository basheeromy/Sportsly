
from rest_framework import serializers
from .models import (
    Product,
    Category,
    Size,
    Color
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

class CategorySerializer(serializers.ModelSerializer):
    """Serializer to manage category."""

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'parent'
        ]
        extra_kwargs = {'parent': {'required': False}}

    def create(self, validated_data):
        """Create and return new category"""
        user = (self.context['request']).user
        if user.is_seller == False:
            raise serializers.ValidationError("Register as a seller.")

        category = Category(
            name = validated_data['name'],
        )
        if 'parent' in validated_data.keys():
            category.parent = validated_data['parent']
        category.save()

        return category


class SizeSerializer(serializers.ModelSerializer):
    """Serializer to manage size."""
    class Meta:
        model = Size
        fields = [
            'id',
            'name'
        ]

    def create(self, validated_data):
        """Create and return new size."""

        user = (self.context['request']).user
        if user.is_seller == False:
            raise serializers.ValidationError("Register as a seller.")

        size = Size(
            name = validated_data['name'],
        )
        size.save()

        return size
