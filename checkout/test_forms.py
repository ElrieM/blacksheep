# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from .forms import OrderForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutForm(TestCase):
    """
    Checkout form testing class
    """
    def test_add_order_form(self):
        """
        Test order form object
        """
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@email.com',
            'phone_number': '1234567890',
            'country': 'JE',
            'town_or_city': 'Test City',
            'street_address1': 'Address line 1',
            'street_address2': 'Address line 2',
            })
        self.assertTrue(form.is_valid())
