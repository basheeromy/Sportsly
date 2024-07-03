from django.contrib import admin
from product import models

from mptt.admin import DraggableMPTTAdmin



class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = models.Category.objects.add_related_count(
                qs,
                models.Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = models.Category.objects.add_related_count(qs,
                 models.Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class Product_Item_Admin(admin.ModelAdmin):
    """Custom admin for product_items."""
    readonly_fields = ('created_on', 'updated_on')



admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Color)
admin.site.register(models.Size)
admin.site.register(models.Product_Image)
admin.site.register(models.Product)
admin.site.register(models.Product_item, Product_Item_Admin)
admin.site.register(models.Banner)
admin.site.register(models.Brand)
admin.site.register(models.Product_review)
