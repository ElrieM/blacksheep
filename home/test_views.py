# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import SimpleTestCase
from django.shortcuts import reverse
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class HomePageTests(SimpleTestCase):
    """
    Test home page loading
    """
    def test_home_page_status_code(self):
        
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1 class="text-center text-light">Quick and Easy T-shirt Printing</h1>')
