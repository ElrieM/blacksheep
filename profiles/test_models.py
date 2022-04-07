# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User

# Internal:
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestProfileModels(TestCase):
    """
    Test Profile model
    """

    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@mail.com',
        )
        test_user.save()

    def test_profile_str_method(self):
        test_user = User.objects.get(username='test_user')
        profile = UserProfile.objects.get(user=test_user)
        self.assertEqual(str(profile), profile.user.username)