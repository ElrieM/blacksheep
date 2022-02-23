# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.utils.translation import gettext_lazy as _

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Category(models.Model):
    """
    Category model class
    """

    class Meta:
        """
        Plural name for class
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(verbose_name=_('Name'),max_length=254)
    friendly_name = models.CharField(max_length=254,null=True,blank=True)

    def __str__(self):
        """
        Returns category name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns friendly name
        """
        return self.friendly_name


class Product(models.Model):
    """
    Product model class
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    stock_code = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=True, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
