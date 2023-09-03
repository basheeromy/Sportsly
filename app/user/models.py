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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    company_name = models.CharField(max_length=250,blank=True,null=True)
    apartment = models.CharField(max_length=250,blank=True,null=True)
    street = models.CharField(max_length=300)
    town = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    pin = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    secondary_mob = models.CharField(max_length=15)
    additional_info = models.TextField(null=True, blank=True)