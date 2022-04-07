# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages
from django.conf import settings
from django.contrib.auth.models import User

# Internal:
from checkout.models import Order
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestCheckoutViews(TestCase):
    """
    Test for checkout views
    """

    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user', password='test_password')
        test_user_superuser = User.objects.create_superuser(
            username='test_user_superuser', password='test_password')

        test_user.save()
        test_user_superuser.save()

        test_user = UserProfile.objects.get(user=test_user)

        Order.objects.create(
            full_name='Test User',
            email='test_email@mail.com',
            phone_number='1234567890',
            county='NL',
            town_or_city='Test City',
            street_address1='Test Address',
            street_address2='Test Address',
            user_profile=test_user
        )

    def test_checkout_view_empty_cart(self):
        response = self.client.get('/checkout/')
        self.assertEqual(
            str(messages[0]), "Cart is Empty")
