# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from decimal import Decimal

# Internal:
from products.models import Product
from designs.models import Mockup
from blacksheep import settings
from .models import Order, OrderLineItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutModel(TestCase):
    """
    Checkout model testing class

    """
    Product.objects.create(
        name='Test User',
        price='99.99',
        stock_code='CHITSH001',
    )
