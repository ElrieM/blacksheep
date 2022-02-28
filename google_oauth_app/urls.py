# Imports
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path, include
from django.contrib.auth.views import LogoutView

# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('', views.index, name='google_login'),
    path('account/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name="logout"),
]
