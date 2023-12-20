"""urls to order related views."""

from django.urls import path

from order.views import (
    OrderAndOrderItemListCreateAPIView,
    UpdateOrderView
)


urlpatterns = [
    path('', OrderAndOrderItemListCreateAPIView.as_view(), name="list-place-order"),
    path('<int:id>', UpdateOrderView.as_view(), name='update-order')
]