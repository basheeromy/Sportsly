"""
Models to manage order related functionalities.
"""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator

from core.models import User
from product.models import Product_item
from user.models import (
    Address,
    BillingAddress
)
# from order.task import send_order_details

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

    def delete(self):
        """
        Soft delete order when user cancel the order.
        """
        self.order_status = "Cancelled"
        self.save()


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
    is_delete = models.BooleanField(default=False)

    def delete(self):
        """
        Soft delete order item.
        """
        self.is_delete = True


@receiver(post_save, sender=OrderItem)
def created_user(sender, created, instance, **kwargs):
    if created:
        pass
        """print(
            f"new order for {instance.product} created successfully. sender is {sender} "
            f"address is {instance.order.shipping_address} "
            f"and billing address is {instance.order.billing_address}"

        )"""

# @receiver(post_save, sender=OrderItem)
# def post_create_functions(sender, created, instance, **kwargs):
#     if created:
#         product = instance.product.__str__()
#         quantity = instance.quantity
#         shipping_address = instance.order.shipping_address.__str__()
#         billing_address = instance.order.billing_address.__str__()
#         user = instance.order.user.__str__()

#         send_order_details.delay(
#             product,
#             quantity,
#             shipping_address,
#             billing_address,
#             user
#         )


