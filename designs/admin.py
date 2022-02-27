# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# internal:
from .models import Mockup, Elements
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MockupAdmin(admin.ModelAdmin):
    """
    Design tempate admin class
    """
    list_display = (
        'friendly_name',
        'name',
        'price',
        'image',
    )


class ElementsAdmin(admin.ModelAdmin):
    """
    Design elements admin class
    """
    list_display = (
        'name',
        'file_id',
        'image',
    )
    
admin.site.register(Mockup)
admin.site.register(Elements)
