"""urls to cart related views."""

from django.urls import path

from cart.views import (
    AddCartItemView,
)

urlpatterns = [
    path('add_item', AddCartItemView.as_view(), name="add_to_cart"),
]
