from django.contrib import admin
from product import models

class Product_Item_Admin(admin.ModelAdmin):
    """Custom admin for product_items."""
    readonly_fields = ('created_on', 'updated_on')



admin.site.register(models.Category)
admin.site.register(models.Color)
admin.site.register(models.Size)
admin.site.register(models.Product_Image)
admin.site.register(models.Product)
admin.site.register(models.Product_item, Product_Item_Admin)
