"""urls to wish list related views."""

from django.urls import path

from .views import (
    ListCreateWishListView
)


urlpatterns = [
    path('', ListCreateWishListView.as_view(), name="add_to_wishlist"),

]