# userprofile/urls.py

from django.urls import path
from .views import sample_profile

urlpatterns = [
    path('sample/', sample_profile),
]
