from dataclasses import fields
from rest_framework import serializers
from .models import (
    Product,
    Product_item
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'size'
        )