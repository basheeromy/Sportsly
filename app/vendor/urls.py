"""URL mapping for the vendor API"""

from django.urls import path
from vendor.views import (
    CreateVendorView,
    ListCreateProductView,
    UpdateProductView,
    ListCreateCategoryView,
    UpdateCategoryView,
    ListCreateSizeView,
    UpdateSizeView,
    ListCreateColorView,
    UpdateColorView
)

urlpatterns = [
    path('create/', CreateVendorView.as_view(), name='create_vendor'),
    path('list-create-product', ListCreateProductView.as_view(), name='list-create-product'),
    path('update-product', UpdateProductView.as_view(), name='update-product'),
    path('list-create-category', ListCreateCategoryView.as_view(), name='list-create-category'),
    path('update-category', UpdateCategoryView.as_view(), name='update-category'),
    path('list-create-size', ListCreateSizeView.as_view(), name='list-create-size'),
    path('update-size', UpdateSizeView.as_view(), name='update-size'),
    path('list-create-color', ListCreateColorView.as_view(), name='list-create-color'),
    path('update-color', UpdateColorView.as_view(), name='update-color')
]
