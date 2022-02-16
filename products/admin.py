# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# internal:
from .models import Category, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ProductAdmin(admin.ModelAdmin):
    """
    Product model admin class
    """
    list_display = (
        'stock_code',
        'name',
        'category',
        'has_sizes',
        'price',
        'image',
        'image2',
        'image_url',
    )
    list_filter = (
        'category',
        'name',
        'price',
    )
    search_fields = (
        'category',
        'name',
        'price',
    )
    
    ordering = ('stock_code',)

class CategoryAdmin(admin.ModelAdmin):
    """
    Category model admin class
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
