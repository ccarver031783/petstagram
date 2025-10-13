from django.http import JsonResponse
from .models import UserProfile
from django.shortcuts import render

def sample_profile(request):
    profile = UserProfile.objects.first()
    if profile:
        return JsonResponse({
            'user': profile.user.username,
            'bio': profile.bio,
            'location': profile.location,
        })
    return JsonResponse({'error': 'No profile found'}, status=404)

def react_home(request):
    return render(request, 'index.html')