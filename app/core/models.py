"""Create user models"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, mobile, password=None, **extra_fields):
        """Create, save and return a new user."""

        if not email:
            raise ValueError('User must have an email address.')

        user = self.model(email=self.normalize_email(email),mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, mobile, password=None, **extra_fields):
        """Create and return new super user."""
        user=self.create_user(email, mobile, password, **extra_fields)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    """
    Model for all users in the project. including,
    customer, seller/vendor, admin.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
