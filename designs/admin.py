# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# internal:
from .models import Mockup, Design
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MockupAdmin(admin.ModelAdmin):
    """
    Design tempate admin class
    """
    list_display = (
        'friendly_name',
        'name',
        'base_price',
        'image',
    )

class DesignAdmin(admin.ModelAdmin):
    """
    Design tempate admin class
    """
    list_display = (
        'stock_code',
        'name',
        'price',
        'image',
    )

admin.site.register(Mockup)
admin.site.register(Design)
