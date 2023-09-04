# Register models for admin side.

from django.contrib import admin
from .models import *

admin.site.register(Order)
admin.site.register(OrderItem)