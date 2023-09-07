"""
Models to manage order related functionalities.
"""
from django.db import models
from django.core.validators import MinValueValidator

from core.models import User
from product.models import Product_item
from user.models import (
    Address,
    BillingAddress
)


class Order(models.Model):
    """Medel to manage orders"""
    PAYMENT_MODES = [
        ("COD", "Cash On Delivery"),
        ("CC", "Credit Card"),
        ("DC", "Debit Card"),
        ("UPI", "Unified Payment Interface"),
        ("NB", "Net Banking"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Owner")
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=250)
    payment_mode = models.CharField(max_length=3, choices=PAYMENT_MODES)
    payment_status = models.CharField(max_length=200)


class OrderItem(models.Model):
    """Model to manage order items"""
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderitem_set")
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Seller")
    product = models.ForeignKey(Product_item, on_delete=models.PROTECT)
    quantity = models.IntegerField(
            default=0,
            validators=[MinValueValidator(0)]
            )
    price = models.DecimalField(max_digits=10, decimal_places=2)
