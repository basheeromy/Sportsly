from django.urls import path

from .views import (
    ProductListView,
    ProductItemListView,
)


urlpatterns = [
    path('list-product/', ProductListView.as_view(), name="latest-products"),
    path('list-product-item/', ProductItemListView.as_view(), name="latest-product-items")
]