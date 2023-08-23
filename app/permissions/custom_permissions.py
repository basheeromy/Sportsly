"""Define Custom permissions."""

from rest_framework.permissions import BasePermission


class IsSellerUser(BasePermission):
    """
    Allows access only to users registered as seller.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_seller)