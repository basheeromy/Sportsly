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
        'create/',
        CreateVendorView.as_view(),
        name='create_vendor'
    ),

    path(
        'list-create-product',
        ListCreateProductView.as_view(),
        name='list-create-product'
    ),

    path(
        'list-create-product-item',
        ListCreateProductItemView.as_view(),
        name='list-create-product-item'
    ),

    path(
        'update-delete-product-item/<int:id>',
        UpdateDeleteProductItemView.as_view(),
        name='update-delete-product-item'
    ),

    path(
        'update-delete-product/<int:id>',
        UpdateDeleteProductView.as_view(),
        name='update-product'
    ),

    path(
        'list-create-category',
        ListCreateCategoryView.as_view(),
        name='list-create-category'
    ),

    path(
        'update-delete-category/<int:id>',
        UpdateDeleteCategoryView.as_view(),
        name='update-delete-category'
    ),

    path(
        'list-create-size',
        ListCreateSizeView.as_view(),
        name='list-create-size'
    ),

    path(
        'update-delete-size/<int:id>',
        UpdateDeleteSizeView.as_view(),
        name='update-size'
    ),

    path(
        'list-create-color',
        ListCreateColorView.as_view(),
        name='list-create-color'
    ),

    path(
        'update-delete-color/<int:id>',
        UpdateDeleteColorView.as_view(),
        name='update-color'
    ),

    path(
        'list-create-image',
        ListCreateImageView.as_view(),
        name='list-images'
    ),

    path(
        'update-delete-image/<int:id>',
        UpdateDeleteImageView.as_view(),
        name='update-color'
    ),
]
