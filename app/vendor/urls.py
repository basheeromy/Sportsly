"""URL mapping for the vendor API"""

from django.urls import path
from vendor.views import (
    CreateVendorView,
    ListCreateProductView,
    UpdateProductView,
    ListCreateCategoryView,
)

urlpatterns = [
    path('create/', CreateVendorView.as_view(), name='create_vendor'),
    path('list-create-product', ListCreateProductView.as_view(), name='list-create-product'),
    path('update-product', UpdateProductView.as_view(), name='update-product'),
    path('list-create-category', ListCreateCategoryView.as_view(), name='list-create-category'),
]
