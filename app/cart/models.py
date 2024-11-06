"""
Models to manage database of carts.
"""
from django.db import models
from product.models import Product_item
from core.models import User

from django.core.validators import MinValueValidator

class CartItem(models.Model):
    """
    Model to manage cart items
    """
    product = models.ForeignKey(Product_item, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s Cart with {self.product}"
