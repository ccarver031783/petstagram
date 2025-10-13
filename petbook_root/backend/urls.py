#petbook_root/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to Petbook!"), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('backend.accounts.urls')),
]
