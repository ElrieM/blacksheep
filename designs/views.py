# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Mockup
from .forms import MockupForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def designs(request):
    """
    A view to show categories and design for design template.
    User selects category, then product, which loads design page.
    """
    mockups = Mockup.objects.all()

    context = {
        'mockup': mockups,
    }

    return render(request, 'designs/designs.html', context)


def design_mockup(request, mockup_id):
    """
    A view with selected product type in background, canvas overlay for
    design input and export design file
    """
    mockup = get_object_or_404(Mockup, pk=mockup_id)

    context = {
        'mockup': mockup,
    }
    
    return render(request, 'designs/design_mockup.html', context)


@login_required
def add_mockup(request):
    """
    A view for adding new mockup templates. Only administrative users can make changes.
    """
    if not request.user.is_superuser:
        messages.error(request, "This action can only be performed by super users.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MockupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New design template added successfully')
            return redirect(reverse('add_mockup'))
        else:
            messages.error(request, 'An error occurred when attempting to add new design template. \
                Please check form is valid and try again')
    else:
        form = MockupForm()

    template = 'designs/add_mockup.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_mockup(request, mockup_id):
    """
    A view for editing existing mockup templates. Only administrative users can make changes.
    """
    if not request.user.is_superuser:
        messages.error(request, "This action can only be performed by super users.")
        return redirect(reverse('home'))


    mockup = get_object_or_404(Mockup, pk=mockup_id)
    if request.method == 'POST':
        form = MockupForm(request.POST, request.FILES, instance=mockup)
        if form.is_valid():
            form.save()
            messages.success(request, 'Design template details updated successfully')
            return redirect(reverse('design_mockup', args=[mockup.id]))
        else:
            messages.error(request, 'Design template update failed.\
                Please review form details and resubmit')
    else:
        form = MockupForm(instance=mockup)
        messages.info(request, f'You are editing {mockup.name}')

    template = 'designs/edit_mockup.html'
    context = {
        'form': form,
        'mockup': mockup,
    }

    return render(request, template, context)


@login_required
def delete_mockup(request, mockup_id):
    """
    A view to delete a mockup template.
    """
    if not request.user.is_superuser:
        messages.error(request, "This action can only be performed by site administrators.")
        return redirect(reverse('home'))

    mockup = get_object_or_404(Mockup, pk=mockup_id)
    mockup.delete()
    messages.success(request, 'Design template removed')

    return redirect(reverse('designs'))
