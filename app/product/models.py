"""Models to manage products."""
import uuid
import os
from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)
from PIL import Image # noqa
from core.models import User
from django.utils import timezone
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models import Avg

# from cart.models import WishList


def category_image_file_path(instance, filename):
    """Generate file path for new category image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'category', filename)

class Category(MPTTModel):
    """Manage product categories with hierarchy."""

    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children'
    )
    info = models.TextField(
        null=True,
        blank=True
    )
    path = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=category_image_file_path
    )


    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Color(models.Model):
    """Color options for products."""
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_seller": True}
    )

    def __str__(self):
        return self.name


class Size(models.Model):
    """Size options for products."""
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_seller": True}
        )

    def __str__(self):
        return self.name


# class ProductQuerySet(models.QuerySet):

#     def with_first_item(self):

#         first_item_subquery = Product_item.objects.filter(
#             name=models.OuterRef('pk')
#         ).order_by('updated_on').values('pk')[:1]

#         return self.annotate(
#             first_item_id=models.Subquery(
#                 first_item_subquery
#             )
#         )


# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return ProductQuerySet(
#             self.model,
#             using=self._db
#         ).with_first_item()


class Brand(models.Model):
    """Manage Brands."""

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        User,
        related_name='owner_of_brand',
        on_delete=models.CASCADE,

        limit_choices_to={"is_seller": True}
    )

    def __str__(self):
        return(self.name)


class Tag(models.TextChoices):
    trending = 'Trending'
    new_arrival = 'New Arrival'
    best_seller = 'Best Seller'
    limited_edition = 'Limited Edition'
    top_rating = 'Top Rating'


class Product(models.Model):
    """Manage Products."""
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand,
        related_name='brand_of_the_product',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category, blank=True)
    tag = models.CharField(
        max_length=20,
        choices=Tag.choices,
        null=True,
        blank=True
    )
    owner = models.ForeignKey(
        User,
        related_name="Seller_of_product",
        on_delete=models.CASCADE,
        limit_choices_to={"is_seller": True}
    )
    is_active = models.BooleanField(default=True)

    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg('rating')) or 0.0

    # objects = ProductManager()

    def __str__(self):
        return self.name


class Product_item(models.Model):
    """Model to manage variants of a particular product"""
    name = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="item"
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
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99)
        ]
    )
    created_on = models.DateTimeField(editable=False)
    updated_on = models.DateTimeField(editable=False)
    is_active = models.BooleanField(default=True)
    coupon = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

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

class Product_review(models.Model):
    """
        Model to handle product reviews
        and ratings.
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='product_reviews'
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5.00)
        ]
    )
    comment = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Review of {self.product.name} by {self.user.name}'


class Product_Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=product_image_file_path)
    product = models.ForeignKey(
        Product_item,
        related_name="images",
        on_delete=models.CASCADE
    )
    # owner = models.ForeignKey(User, related_name="Uploaded_seller", on_delete=models.CASCADE)
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
    """Generate file path for new banner image."""
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

    path = models.CharField(max_length=255)


    vendor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_seller": True}
    )
    validity = models.DateTimeField(null=True, blank=True)
