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
    def setup(self):
        Product.objects.create(
            name='Test User',
            price='99.99',
            stock_code='CHITSH001',
            description='Test description',
        )

        Order.objects.create(
            full_name='Test Name',
            email='test@email.com',
            phone_number='1234567890',
            country='NL',
            town_or_city='Test City',
            street_address1='Test Address',
        )

    def test_order_str_method(self):
        order = Order.objects.get(email='test@email.com')
        self.assertEqual(str(order), order.order_number)
