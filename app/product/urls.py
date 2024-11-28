from django.urls import path

from .views import (
    ProductListView,
    ProductItemListView,
    ListBanners,
    ListCategoryTreeAPIView,
    ProductTileListView,
    ProductItemDetailView,
    productReviewListView
)


urlpatterns = [
    path('list-product/', ProductListView.as_view(), name="latest-products"),
    path('list-product-item/', ProductItemListView.as_view(), name="latest-product-items"),
    path('list-banners/', ListBanners.as_view(), name='list-banners'),
    path('list-categories', ListCategoryTreeAPIView.as_view(), name='list-categories'),
    path('list-product-tiles/',ProductTileListView.as_view(), name='product-tile-list' ),
    path('detail/<int:id>', ProductItemDetailView.as_view(), name='product-item-details'),
    path('detail/<int:product_id>/reviews', productReviewListView.as_view(), name='product-review-list')
]