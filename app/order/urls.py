"""urls to order related views."""

from django.urls import path

from order.views import (
    OrderAndOrderItemListCreateAPIView
)


urlpatterns = [
    path('add_item', OrderAndOrderItemListCreateAPIView.as_view(), name="add_to_cart"),
]