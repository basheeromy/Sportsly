"""URL mapping for the user API"""

from django.urls import path

from rest_framework_simplejwt.views import (
    #TokenObtainPairView,
    TokenRefreshView
)

from user.views import (
    CreatUserView,
    GenerateOtpView,
    VerifyOTPView,
    GenerateTokenView,
    ManageUserView,
    ListAllUserView

)

app_name = 'user'


urlpatterns = [
    path('create/', CreatUserView.as_view(), name='create'),
    path('update/', ManageUserView.as_view(), name="update"),
    path('token/', GenerateTokenView.as_view(), name='token_obtain_pair'),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('generate-otp/', GenerateOtpView.as_view(), name='generate_otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('list-all-user', ListAllUserView.as_view(), name='list_all_user'),
]
