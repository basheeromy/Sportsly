"""urls to cart related views."""

from django.urls import path

from cart.views import (
    AddCartItemView,
    UpdateDeleteCartItem
)
"""path('delete_item', DeleteCartItem.as_view(), name="delete_cart_item")
path('update_item', UpdateCartView.as_view(), name="add_to_cart"),"""

urlpatterns = [
    path('', AddCartItemView.as_view(), name="add_to_cart"),
    path('<int:id>', UpdateDeleteCartItem.as_view(), name="delete_cart_item")
]
