"""URL mapping for the vendor API"""

from django.urls import path
from vendor.views import (
    CreateVendorView,
    ListCreateProductView,
    UpdateDeleteProductView,
    ListCreateProductItemView,
    UpdateDeleteProductItemView,
    ListCreateCategoryView,
    UpdateDeleteCategoryView,
    ListCreateSizeView,
    UpdateDeleteSizeView,
    ListCreateColorView,
    UpdateDeleteColorView,
    ListCreateImageView,
    UpdateDeleteImageView
)

urlpatterns = [
    path(
        '',
        CreateVendorView.as_view(),
        name='create_vendor'
    ),

    path(
        'product',
        ListCreateProductView.as_view(),
        name='list-create-product'
    ),

    path(
        'product-item',
        ListCreateProductItemView.as_view(),
        name='list-create-product-item'
    ),

    path(
        'product-item/<int:id>',
        UpdateDeleteProductItemView.as_view(),
        name='update-delete-product-item'
    ),

    path(
        'product/<int:id>',
        UpdateDeleteProductView.as_view(),
        name='update-product'
    ),

    path(
        'category',
        ListCreateCategoryView.as_view(),
        name='list-create-category'
    ),

    path(
        'category/<int:id>',
        UpdateDeleteCategoryView.as_view(),
        name='update-delete-category'
    ),

    path(
        'size',
        ListCreateSizeView.as_view(),
        name='list-create-size'
    ),

    path(
        'size/<int:id>',
        UpdateDeleteSizeView.as_view(),
        name='update-size'
    ),

    path(
        'color',
        ListCreateColorView.as_view(),
        name='list-create-color'
    ),

    path(
        'color/<int:id>',
        UpdateDeleteColorView.as_view(),
        name='update-color'
    ),

    path(
        'image',
        ListCreateImageView.as_view(),
        name='list-images'
    ),

    path(
        'image/<int:id>',
        UpdateDeleteImageView.as_view(),
        name='update-color'
    ),
]
