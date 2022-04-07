# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('', views.designs, name="designs"),

    path('mockup/', views.designs, name="designs"),
    path('mockup/<int:mockup_id>/', views.design_mockup, name="design_mockup"),
    path('mockup/delete/<int:design_id>/', views.delete_design, name="delete_design"),
    path('<int:design_id>/', views.design_detail, name='design_detail'),

    path('add/', views.add_template, name="add_template"),
    path('edit/<int:mockup_id>', views.edit_template, name="edit_template"),
    path('delete/<int:mockup_id>', views.delete_template, name="delete_template"),
]
