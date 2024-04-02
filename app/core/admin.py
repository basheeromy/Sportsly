"""Django admin customization."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin page for users."""
    ordering = ['id']
    list_display = ['email', 'mobile', 'name', 'gender']
    fieldsets = (
        (None,  {'fields': ('email', 'mobile', 'password')}),
        (
            _('permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'is_seller',
                    'gender'
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    read_only_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'mobile',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
                'is_seller',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
