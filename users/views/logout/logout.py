
# Django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse


@login_required
def logout_view(request):
    """Logout view."""
    logout(request)
    return redirect('user_login')


@login_required
def logout_json(request):
    """Logout view json."""
    return JsonResponse({'logout': logout(request)})
