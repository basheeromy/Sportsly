"""Views for the Create user API"""

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from django.conf import settings

from user.serializers import (
    UserSerializer,
    GenerateOtpSerializer,
    ValidateOtpSerializer,
    GenerateTokenSerializer
    )
from django.contrib.auth import get_user_model

from drf_spectacular.utils import extend_schema
import requests
import math
import random


class CreatUserView(CreateAPIView):
    """Create a new Customer user."""
    serializer_class = UserSerializer


class GenerateTokenView(APIView):
    @extend_schema(request=GenerateTokenSerializer, responses=None)
    def post(self, request, *args, **kwargs):
        serializer = GenerateTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        refresh = RefreshToken.for_user(data)
        return Response({'refresh': str(refresh),
                         'access': str(refresh.access_token),
        })

def send_otp(phone):
    """
    This is an helper function to send otp to phone number
    passed as an argument to this function.

    Args:
        phone (string): mobile to send otp to.
    """

    if phone:

        digits = "0123456789"
        otp = ""
        for i in range(6):
            otp += digits[math.floor(random.random() * 10)]

        phone = str(phone)
        #link = f'https://2factor.in/API/V1/{settings.OTP_API_KEY}/SMS/+91{phone}/{otp}/OTP-1' # noqa
        #result = requests.get(link, verify=False)
        #print(result)
        print(otp)
        return otp
    else:
        return False


class GenerateOtpView(APIView):
    @extend_schema(request=GenerateOtpSerializer, responses=None)
    def post(self, request, *args, **kwargs):
        serializer = GenerateOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            phone_number = serializer.validated_data.get('mobile')
            mobile = str(phone_number)

            data = get_user_model().objects.get(mobile__iexact=mobile)
            new_otp = send_otp(mobile)
            data.otp = new_otp
            data.save()

            return Response({
                'message': 'OTP sent successfully.',
                'status': HTTP_200_OK,
            })

        except Exception as e:
            print(e)
            return Response({
                'message': str(e),
                'status': HTTP_400_BAD_REQUEST,
            })


class VerifyOTPView(APIView):
    """Verify the given OTP."""
    @extend_schema(request=ValidateOtpSerializer, responses=None)
    def post(self, request, *args, **kwargs):
        serializer = ValidateOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print()
        try:

            user = serializer.validated_data.get('mobile')
            user = user.first()

            print(user.name)
            otp = request.data.get('otp')
            if user.otp == otp:
                user.is_active = True
                user.save()
                return Response({
                    'message': 'OTP verification successful.',
                    'status': HTTP_200_OK,
                })
            else:
                return Response({
                    'message': 'OTP does not match.',
                    'status': HTTP_400_BAD_REQUEST
                })
        except Exception as e:
            return Response({
                'status': False,
                'message': str(e),
                'details': 'OTP Verification failed'
            })


