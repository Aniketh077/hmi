# hmiapp/urls.py

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    # Add more URL patterns as needed
]
