# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms

# Internal:
from .widgets import CustomClearableFileInput
from .models import Mockup
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
