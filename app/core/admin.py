"""Django admin customization."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin page for users."""
    ordering = ['id']
    list_display = ['email','mobile','name']
admin.site.register(models.User, UserAdmin)