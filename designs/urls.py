# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('', views.design_overview, name="designs"),
    path('design/', views.design_mockup, name="design_mockup"),
    path('add/', views.add_mockup, name="add_mockup"),
    path('edit/', views.edit_mockup, name="edit_mockup"),
    path('delete/', views.delete_mockup, name="delete_mockup"),
]
