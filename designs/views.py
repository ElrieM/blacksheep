# Imports 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def design_overview(request):
    """
    A view to show categories and design for design template.
    User selects category, then product, which loads design page.
    """
    return render(request, 'designs/design_overview.html')


def design_mockup(request):
    """
    A view with selected product type in background, canvas overlay for design input and export design file
    """
    return render(request, 'designs/design_mockup.html')


def add_mockup(request):
    """
    A view for adding new mockup templates. Only administrative users can make changes.
    """
    return render(request, 'designs/add_mockup.html')


def edit_mockup(request):
    """
    A view for editing existing mockup templates. Only administrative users can make changes.
    """
    return render(request, 'designs/edit_mockup.html')


def delete_mockup(request):
    """
    A view to delete a mockup template.
    """
    return redirect(reverse('designs'))
