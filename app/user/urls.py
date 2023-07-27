"""URL mapping for the user API"""

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user.views import (
    CreatUserView,
    GenerateOtpView,
    VerifyOTPView,
)

app_name = 'user'


urlpatterns = [
    path('create/', CreatUserView.as_view(), name='create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('generate-otp/', GenerateOtpView.as_view(), name='generate_otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
]
