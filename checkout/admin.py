# Imports 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Order, OrderLineItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class OrderLineItemAdminInline(admin.TabularInline):
    """
    OrderLineItem admin class
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Order admin class
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number',
                       'order_date',
                       'delivery_cost',
                       'order_total',
                       'grand_total',)

    fields = ('order_number',
              'order_date',
              'full_name',
              'email',
              'phone_number',
              'country',
              'postcode',
              'town_or_city',
              'street_address1',
              'street_address2',
              'county',
              'delivery_cost',
              'order_total',
              'grand_total')

    list_display = ('order_number',
                    'order_date',
                    'full_name',
                    'order_total',
                    'delivery_cost',
                    'grand_total',)

    ordering = ('-order_date',)

admin.site.register(Order, OrderAdmin)
