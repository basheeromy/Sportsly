"""
Models to manage user related data like
Adress,
"""

from django.db import models
from core.models import User
from product.models import Product_item


class Address(models.Model):
    """
        Model to define the Address table.
    """
    TAG_CHOICES = (
        ('HOME', 'Home'),
        ('OFFICE', 'Office')
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owner"
    )
    apartment = models.CharField(max_length=250, blank=True, null=True)
    street = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    pin = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    secondary_mob = models.CharField(max_length=15, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    tag = models.CharField(
        max_length=10,
        choices=TAG_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.name}'s Address"


class BillingAddress(models.Model):
    """
        Model to define Billing Address table.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the billing address to a user
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    company_name = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    gst_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.name}'s Billing Address"
