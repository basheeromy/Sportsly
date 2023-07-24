"""URL mapping for the user API"""

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user import views

app_name = 'user'


urlpatterns = [
    path('create/', views.CreatUserView.as_view(), name='create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
