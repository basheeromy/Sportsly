"""URL mapping for the vendor API"""

from django.urls import path
from vendor.views import (
    CreateVendorView,
    CreateProductView,
    ListProductView,
    UpdateProductView,
    ListCategoryView
    #ManageProductView
)

urlpatterns = [
    path('create/', CreateVendorView.as_view(), name='create_vendor'),
    path('create-product', CreateProductView.as_view(), name='create_product'),
    path('list-product', ListProductView.as_view(), name='list-product'),
    path('update-product', UpdateProductView.as_view(), name='update-product'),
    path('list-category', ListCategoryView.as_view(), name='list-category')
]
