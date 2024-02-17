from django.urls import path

from .views import (
    ProductListView,
    ProductItemListView,
    ListBanners,
    ListCategoryTreeAPIView
)


urlpatterns = [
    path('list-product/', ProductListView.as_view(), name="latest-products"),
    path('list-product-item/', ProductItemListView.as_view(), name="latest-product-items"),
    path('list-banners/', ListBanners.as_view(), name='list-banners'),
    path('list-categories', ListCategoryTreeAPIView.as_view(), name='list-categories')
]