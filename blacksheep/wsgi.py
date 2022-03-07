"""
WSGI config for blacksheep project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
import os

# Internal:
from django.core.wsgi import get_wsgi_application
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blacksheep.settings')

application = get_wsgi_application()
