# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

# Internal:
from checkout.models import Order
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestProfileViews(TestCase):
    """
    Test Profile views
    """

    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@mail.com',
        )
        test_user.save()

    Order.objects.create(
        order_number='12345',
        user_profile=UserProfile.objects.get(user=test_user),
        full_name='Test User',
        email='test_user@test.com',
        phone_number='1234567890',
        country='NL',
        postcode='1234AA',
        street_address1='Test address',
        county='Test Town',
    )

    def test_get_profile_page(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_post_profile_page(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.post('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
    
    def test_get_order_detail_page(self):
        self.client.login(username='test_user', password='test_password')
        test_user = User.objects.get(username='test_user')
        order = Order.objects.get(email=test_user.email)
        response = self.client.get('/profile/order_history/' + order.order_number)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                        'This is a past confirmation for order number 12345. ' +
                        'A confirmation email was sent on the order date.')
