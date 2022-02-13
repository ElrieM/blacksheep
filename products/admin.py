# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# internal:
from .models import Category, Subcategory, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ProductAdmin(admin.ModelAdmin):
    """
    Product model admin class
    """
    list_display = (
        'stock_code',
        'name',
        'category',
        'subcategory',
        'has_sizes',
        'price',
        'image',
        'image2',
        'image_url',
    )
    list_filter = (
        'category',
        'subcategory',
        'name',
        'price',
    )
    search_fields = (
        'category',
        'subcategory',
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


class SubcategoryAdmin(admin.ModelAdmin):
    """
    Subcategory model admin class
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
