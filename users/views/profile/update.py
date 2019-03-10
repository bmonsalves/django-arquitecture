
# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse


@login_required
def update(request):
    """update profile view."""
    profile = request.user.profile

    # NOT IMPLEMENTED

    return render(request, 'update_profile.html', {'profile': profile})


@login_required
def update_json(request):
    """update profile json."""
    profile = request.user.profile

    # NOT IMPLEMENTED
    return JsonResponse({'profile': profile})
