"""URL mapping for the user API"""

from django.urls import path

from rest_framework_simplejwt.views import (
    #TokenObtainPairView,
    TokenRefreshView
)

from user.views import (
    CreateUserView,
    GenerateOtpView,
    VerifyOTPView,
    GenerateTokenView,
    ManageUserView,
    ListAllUserView,
    ListAddAddressView,
    UpdateDeleteAddressView


)

app_name = 'user'


urlpatterns = [
    path('', CreateUserView.as_view(), name='create'),
    path('manage/', ManageUserView.as_view(), name="update"),
    path('token/', GenerateTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('generate-otp/', GenerateOtpView.as_view(), name='generate_otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('list-all-user', ListAllUserView.as_view(), name='list_all_user'),
    path('address', ListAddAddressView.as_view(), name='add_list_adress'),
    path('address/<int:id>', UpdateDeleteAddressView.as_view(), name='update_delete_address'),
]
