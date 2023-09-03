# Register models for admin site

from django.contrib import admin

from user.models import Address


admin.site.register(Address)