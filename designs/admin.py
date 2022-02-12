# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# internal:
from .models import Mockup
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MockupAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'price',
        'image',
    )

admin.site.register(Mockup)
