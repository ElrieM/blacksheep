# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Class StaticStorage(S3Boto3Storage):
    """
    Class for AWS boto3 storage for static files
    """
    location = settings.STATICFILES_LOCATION


Class MediaStorage(S3Boto3Storage):
    """
    Class for AWS boto3 storage for media files
    """
    location = settings.MEDIAFILES_LOCATION
