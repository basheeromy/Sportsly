"""URL mapping for the vendor API"""

from django.urls import path
from vendor.views import (
    CreateVendorView,
)

urlpatterns = [
    path('create/', CreateVendorView.as_view(), name='create_vendor')
]
