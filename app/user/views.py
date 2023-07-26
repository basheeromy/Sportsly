"""Views for the Create user API"""

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)

from user.serializers import UserSerializer
from django.contrib.auth import get_user_model

import requests
import math, random


class CreatUserView(CreateAPIView):
    """Create a new Customer user."""
    serializer_class = UserSerializer



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
        link = f'https://2factor.in/API/V1/a8978629-2aca-11ee-addf-0200cd936042/SMS/+91{phone}/{otp}/OTP-1'
        result = requests.get(link, verify=False)
        print(result)
        return otp
    else:
        return False


class ValidateUserGenerateOtpView(APIView):
    """
    Validate given phone number, identify the user and send OTP.
    """
    def post(self, request, *args, **kwargs):
        try:
            phone_number = request.data.get('mobile')

            if phone_number:
                mobile = str(phone_number)
                user = get_user_model().objects.filter(mobile__iexact=mobile)

                if user.exists():
                    data = user.first()
                    new_otp = send_otp(mobile)
                    data.otp = new_otp
                    data.save()
                    return Response({
                        'message': 'OTP sent successfully.',
                        'status': HTTP_200_OK,
                    })
                else:
                    return Response({
                        'message': 'User not found ! please register.',
                        'status': HTTP_404_NOT_FOUND,
                    })

            else:
                return Response({
                    'message': 'Phone number is required.',
                    'status': HTTP_400_BAD_REQUEST
                })
        except Exception as e:
            print(e)
            return Response({
                'message': str(e),
                'status': HTTP_400_BAD_REQUEST,
            })


class VerifyOTPView(APIView):
    """Verify the given otp."""

    def post(self, request, format=None):
        try:
            mobile = request.data.get('mobile')
            otp = request.data.get('otp')
            print(mobile, otp)

            if mobile and otp:
                user = get_user_model().objects.filter(mobile__iexact=mobile)
                if user.exists():
                    user = user.first()
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
                else:
                    return Response({
                        'message': 'User does not exists. Please register.',
                        'status' : HTTP_400_BAD_REQUEST
                    })
            else:
                return Response({
                    'message': 'Mobile number or OTP is missing.',
                    'status' : HTTP_400_BAD_REQUEST
                })

        except Exception as e:
            print(e)
            return Response({
                'status' : False,
                'message' : str(e),
                'details' : 'OTP Verification failed'
            })

