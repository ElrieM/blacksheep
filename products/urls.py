# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('', views.product_overview, name="products"),
    path('design/', views.product_design, name="product_design"),
    path('add/', views.add_product, name="add_product"),
    path('edit/', views.edit_product, name="edit_product"),
    path('delete/', views.delete_product, name="delete_product"),
]
