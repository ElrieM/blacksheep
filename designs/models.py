# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.utils.translation import gettext_lazy as _

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Mockup(models.Model):
    """
    Mockup template model class
    """

    class Meta:
        """
            Plural name for class
        """
        verbose_name_plural = 'Mockups'

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        """
        Returns design template name string
        """
        return str(self.name)
