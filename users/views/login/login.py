
# Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username, ": ", password)
        if user:
            login(request, user)
            return redirect('posts_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid username and password'})

    return render(request, 'login.html')


def login_json(request):
    """Login view json."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'user': user})
        else:
            return JsonResponse({'error': 'Invalid username and password'})

    return JsonResponse({'error': 'Not valid'})
