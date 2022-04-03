# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms

# Internal:
from .widgets import CustomClearableFileInput
from .models import Mockup, Design
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class MockupForm(forms.ModelForm):
    """
    Class for design template management form
    """

    class Meta:
        model = Mockup
        fields = '__all__'

    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field, in self.fields.items():
            field.widget.attrs['class'] = 'border-dark'


class DesignForm(forms.ModelForm):
    """
    Class for design saving form
    """
    class Meta:
        """
        class meta details
        """
        model = Design
        fields = '__all__'

        image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'description': 'Short Description',
        }

        for field_name, field, in self.fields.items():
            field.widget.attrs['class'] = 'border-dark'
