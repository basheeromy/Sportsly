"""Models to manage products."""

from django.db import models
from django.core.validators import MinValueValidator
from PIL import Image # noqa
from core.models import User
from django.utils import timezone


class Category(models.Model):
    """Manage product catergories with hierarchy."""

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    """Color options for products."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    """Size options for products."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Manage Products."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product_item(models.Model):
    """Model to manage variants of a particular product"""
    name = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Product_name"
    )
    SKU = models.CharField(max_length=100, unique=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
        )
    seller = models.ForeignKey(
        User,
        related_name="Seller_of_product",
        on_delete=models.CASCADE
    )
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    created_on = models.DateField(editable=False)
    updated_on = models.DateField(editable=False)
    is_active = models.BooleanField(default=True)
    coupen = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        populate created_on field when creating a new instance,
        and populate updated_on field when updating the instance.
        """

        if not self.id:
            self.created_on = timezone.now()
        self.updated_on = timezone.now()
        return super(Product_item, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} {self.color} {self.size}'


class Product_Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    product = models.ForeignKey(
        Product_item,
        related_name="Product_image",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name} image'
