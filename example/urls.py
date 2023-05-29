# example/urls.py
from django.urls import path,include

from example.views import namepage

urlpatterns = [
    path('', namepage),
]