# Imports 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        Updates order total on save and delete
        """
        import checkout.signals
