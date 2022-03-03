# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def index(request):
    """ View to return index.html """

    return render(request, 'home/index.html')


def terms(request):
    """
    View to return terms and conditions
    """
    return render(request, 'home/terms.html')
