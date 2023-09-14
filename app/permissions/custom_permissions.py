"""Define Custom permissions."""

from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser

class IsSellerUser(BasePermission):
    """
    Allows access only to users registered as seller.
    """

    def has_permission(self, request, view):
        if request.user.id == None:
            return False
        return bool(request.user and request.user.is_seller)


class IsOwnerOrReadOnly(BasePermission):
    """
    Allows access only to owner of the database object
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsSellerOrReadOnly(BasePermission):
    """
    Allows access only to owner of the database object
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner