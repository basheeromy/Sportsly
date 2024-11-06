"""
    Models to manage wish list.
"""

from django.db import models
from product.models import Product_item
from core.models import User

class WishList(models.Model):
    """
        Model to define the Wish list table.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_item = models.ForeignKey(
        Product_item,
        on_delete=models.PROTECT,
        related_name='wishlist'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}'s Wish List with {self.product_item}"