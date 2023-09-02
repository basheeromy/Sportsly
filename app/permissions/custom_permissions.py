"""Define Custom permissions."""

from rest_framework.permissions import BasePermission


class IsSellerUser(BasePermission):
    """
    Allows access only to users registered as seller.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_seller)


class IsOwnerOrReadOnly(BasePermission):
    """
    Allows access only to owner of the database object
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user