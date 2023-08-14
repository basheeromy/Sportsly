
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
            'parent',
            'created_by'
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
        category.created_by = validated_data['created_by']
        category.save()

        return category


class SizeSerializer(serializers.ModelSerializer):
    """Serializer to manage size."""
    class Meta:
        model = Size
        fields = [
            'id',
            'name',
            'created_by'
        ]

    def create(self, validated_data):
        """Create and return new size."""

        user = (self.context['request']).user
        if user.is_seller == False:
            raise serializers.ValidationError("Register as a seller.")

        size = Size(
            name = validated_data['name'],
        )
        size.created_by = validated_data['created_by']
        size.save()

        return size

class ColorSerializer(serializers.ModelSerializer):
    """Serializer to manage product color."""

    class Meta:
        model = Color
        fields = [
            'id',
            'name',
            'created_by'
        ]

    def create(self, validated_data):
        """Create and return new color."""

        user = (self.context['request']).user
        if user.is_seller == False:
            raise serializers.ValidationError("Register as a seller.")

        color = Color(
            name = validated_data['name']
        )
        color.created_by = validated_data['created_by']
        color.save()

        return color