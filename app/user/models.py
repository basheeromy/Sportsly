"""
Models to manage user related data like
Adress,
"""

from django.db import models
from core.models import User


class Address(models.Model):
    """Manage delivery address."""

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owner"
    )
    company_name = models.CharField(max_length=250, blank=True, null=True)
    apartment = models.CharField(max_length=250, blank=True, null=True)
    street = models.CharField(max_length=300)
    town = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    pin = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    secondary_mob = models.CharField(max_length=15)
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name}'s Address"


class BillingAddress(models.Model):
    """Manage deleivery address"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the billing address to a user
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.name}'s Billing Address"
