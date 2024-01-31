"""Models to manage products."""
import uuid
import os
from django.db import models
from django.core.validators import MinValueValidator
from PIL import Image # noqa
from core.models import User
from django.utils import timezone
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey



class Category(MPTTModel):
    """Manage product catergories with hierarchy."""

    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children'
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Color(models.Model):
    """Color options for products."""
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Size(models.Model):
    """Size options for products."""
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Manage Products."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category, blank=True)
    owner = models.ForeignKey(
        User,
        related_name="Seller_of_product",
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product_item(models.Model):
    """Model to manage variants of a particular product"""
    name = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="productitem_set"
    )
    SKU = models.CharField(max_length=100, unique=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
        )

    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    created_on = models.DateTimeField(editable=False)
    updated_on = models.DateTimeField(editable=False)
    is_active = models.BooleanField(default=True)
    coupen = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('-updated_on',)

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


def product_image_file_path(instance, filename):
    """Generate file path for new product image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'product', filename)

class Product_Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=product_image_file_path)
    product = models.ForeignKey(
        Product_item,
        related_name="Product_image",
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(User, related_name="Uploaded_seller", on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} image'


class Displays(models.TextChoices):
    """
    Banner position choices.
    """
    Home = 'Home'
    Category = 'Category'
    Profile = 'Profile'


def banner_image_file_path(instance, filename):
    """Generate file path for new product image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'banner', filename)
class Banner(models.Model):
    info = models.TextField(
        null=True,
        blank=True
    )
    display_space = models.CharField(
        max_length=20,
        choices=Displays.choices,
        default=Displays.Profile
    )
    banner_image = models.ImageField(
        upload_to=banner_image_file_path
    )

    # url = models.URLField()
    path = models.CharField(max_length=255)


    vendor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_seller": True}
    )
    validity = models.DateTimeField(null=True, blank=True)
