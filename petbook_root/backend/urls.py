#petbook_root/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from backend.userprofile.views import react_home, sample_profile

urlpatterns = [
    path('', react_home, name='react_home'),
    path('api/profile/', sample_profile, name='sample_profile'),
    path('api/', include('backend.accounts.urls')),
]
