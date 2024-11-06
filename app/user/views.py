"""Views for the Create user API"""

from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    ListCreateAPIView
)

from .task import send_otp

from permissions.custom_permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from django.conf import settings

from user.models import Address
from user.serializers import (
    UserSerializer,
    GenerateOtpSerializer,
    ValidateOtpSerializer,
    GenerateTokenSerializer,
    AddressSerializer
    )
from django.contrib.auth import get_user_model

from drf_spectacular.utils import extend_schema



import math
import random


class CreateUserView(CreateAPIView):
    """Create a new Customer user."""
    serializer_class = UserSerializer

class ManageUserView(RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        print(f"from user profile api {self.request.user}")

        return self.request.user

class GenerateTokenView(APIView):
    """
    View to generate token.
    """

    @extend_schema(request=GenerateTokenSerializer, responses=None)
    def post(self, request, *args, **kwargs):
        serializer = GenerateTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        refresh = RefreshToken.for_user(data)
        return Response({'refresh': str(refresh),
                         'access': str(refresh.access_token),
        })


class GenerateOtpView(APIView):
    """
    View to generate otp.
    """

    @extend_schema(request=GenerateOtpSerializer, responses=None)
    def post(self, request, *args, **kwargs):
        serializer = GenerateOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            phone_number = serializer.validated_data.get('mobile')
            mobile = str(phone_number)
            digits = "0123456789"
            otp = ""
            for i in range(6):
                otp += digits[math.floor(random.random() * 10)]

            send_otp.delay(mobile, otp)
            cache.set(mobile, otp, 600)

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
        try:

            user = serializer.validated_data.get('mobile')
            user = user.first()

            print(user.name)
            otp = request.data.get('otp')
            if cache.get(user.mobile) == otp:
                user.is_active = True
                user.save()
                cache.delete(user.mobile)
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


""" This view is for development purpose. """
class ListAllUserView(ListAPIView):
    """
    View to list all users.
    """

    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=UserSerializer, responses=None)
    def get(self, request, format=None):
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

class ListAddAddressView(ListCreateAPIView):
    """View to add items to cart and list cart items"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer
    queryset = Address.objects.filter()

    def get(self, request, format=None):
        product = Address.objects.filter(user=request.user)
        serializer = AddressSerializer(product, many=True)

        return Response(serializer.data)


class UpdateDeleteAddressView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly

    ]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["id"])
        self.check_object_permissions(self.request, obj)
        return obj
