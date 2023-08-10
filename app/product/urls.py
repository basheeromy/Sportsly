from django.urls import path

from .views import ProductListView


urlpatterns = [
    path('list-product/', ProductListView.as_view(), name="latest-products")
]