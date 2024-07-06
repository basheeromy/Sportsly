
from rest_framework import serializers
from .models import (
    Product,
    Product_item,
    Category,
    Size,
    Color,
    Product_Image,
    Banner
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
        product = Product(
            name=validated_data['name'],
            description=validated_data['description'],
            owner=user,
            is_active=validated_data['is_active']
        )
        product.save()
        product.category.set(validated_data['category'])
        product.save()
        return product


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    class Meta:
        model = Product_Image
        fields = [
            'id',
            'name',
            'image',
            'owner'
        ]

    def create(self, validated_data):
        """Create and return new color."""

        image = Product_Image(
            name=validated_data['name'],
            image=validated_data['image']
        )
        image.product = validated_data['product']
        image.owner = validated_data['owner']  # change to owner.
        image.save()

        return image


class ProductItemSerializer(serializers.ModelSerializer):
    images = ImageSerializer(
        many=True,
        read_only=True
    )
    name = serializers.StringRelatedField()
    size = serializers.StringRelatedField()
    color = serializers.StringRelatedField()

    class Meta:
        model = Product_item
        fields = [
            'id',
            'name',
            'SKU',
            'size',
            'color',
            'price',
            'quantity',
            'discount',
            'created_on',
            'updated_on',
            'is_active',
            'coupon',
            'images'
        ]
        extra_kwargs = {
            'created_on': {
                'required': False,
                'read_only': True
            },
            'updated_on': {
                'required': False,
                'read_only': True
            },
        }

    def create(self, validated_data):
        """Create and return a new product_item."""
        product_item = Product_item(
            name=validated_data['name'],
            SKU=validated_data['SKU'],
            size=validated_data['size'],
            color=validated_data['color'],
            price=validated_data['price'],
            quantity=validated_data['quantity'],
            discount=validated_data['discount'],
            is_active=validated_data['is_active'],
            coupon=validated_data['coupon']
        )
        product_item.save()
        return product_item


class ProductTileSerializer(serializers.ModelSerializer):
    images = ImageSerializer(
        many=True,
        read_only=True
    )
    name = serializers.StringRelatedField()
    brand_name = serializers.StringRelatedField()
    average_rating = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    effective_price = serializers.SerializerMethodField()


    class Meta:
        model = Product_item
        fields = [
            'id',
            'name',
            'price',
            'discount',
            'images',
            'brand_name',
            # 'sales_volume',
            'tag',
            'average_rating',
            'effective_price',
        ]
        extra_kwargs = {
            'created_on': {
                'required': False,
                'read_only': True
            },
            'updated_on': {
                'required': False,
                'read_only': True
            },
        }

    def get_average_rating(self, obj):
        """
            method to fetch average rating
            per product.
        """
        return obj.name.average_rating["rating__avg"]

    def get_tag(self, obj):
        """
            method to fetch tag.
        """
        return obj.name.tag

    def get_effective_price(self, obj):
        """
            method to calculate average
            price.
        """
        effective_price = float(obj.price) - (obj.discount/100)
        return effective_price


class ProductItemListSerializer(serializers.ModelSerializer):
    """
        This serializer helps us to serialize the
        combined data from product and productItem
        table for product_tiles.
    """
    first_item = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'first_item']

    def get_first_item(self, obj):
        try:
            product_item = Product_item.objects.get(pk=obj.first_item_id)
            return ProductItemSerializer(product_item).data
        except Product_item.DoesNotExist:
            return None


class CategorySerializer(serializers.ModelSerializer):
    """Serializer to manage category."""

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'image',
            'path',
            'parent',
        ]
        extra_kwargs = {'parent': {'required': False}}

    def create(self, validated_data):
        """Create and return new category"""

        category = Category(
            name=validated_data['name'],
        )
        if 'parent' in validated_data.keys():
            category.parent = validated_data['parent']
        category.owner = validated_data['created_by']
        category.save()

        return category


class CategoryTreeSerializer(serializers.ModelSerializer):
    """
        Serializer to handle category tree.
    """
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'image',
            'path',
            'children'
        ]

    def get_children(self, obj):

        children = obj.children.all()
        serializer = self.__class__(children, many=True)
        return serializer.data


class SizeSerializer(serializers.ModelSerializer):
    """Serializer to manage size."""
    class Meta:
        model = Size
        fields = [
            'id',
            'name',
            'owner'
        ]

    def create(self, validated_data):
        """Create and return new size."""

        size = Size(
            name=validated_data['name'],
        )
        size.owner = validated_data['created_by']
        size.save()

        return size


class ColorSerializer(serializers.ModelSerializer):
    """Serializer to manage product color."""

    class Meta:
        model = Color
        fields = [
            'id',
            'name',
            'owner'
        ]

    def create(self, validated_data):
        """Create and return new color."""

        color = Color(
            name=validated_data['name']
        )
        color.owner = validated_data['created_by']  # change to owner
        color.save()

        return color


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'banner_image',
            'path'
        ]
