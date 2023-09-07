# Register models for admin site

from django.contrib import admin

from user.models import (
    Address,
    BillingAddress
)


admin.site.register(Address)
admin.site.register(BillingAddress)