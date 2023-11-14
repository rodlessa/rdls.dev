# example/urls.py
from django.urls import path

from example.views import index, cv


urlpatterns = [
    path('', index),
    path('cv', cv),
]