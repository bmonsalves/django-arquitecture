
# Django
from django.db import IntegrityError

from users.models import Profile

from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse


def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        if user:
            login(request, user)
            return redirect('posts_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid username and password'})

    return render(request, 'signup.html')


def signup_json(request):
    """Sign up json."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return JsonResponse({'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return JsonResponse({'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        if user:
            login(request, user)
            return JsonResponse({'user': user, 'profile': profile})
        else:
            return JsonResponse({'error': 'Invalid username and password'})

    return JsonResponse({'logout': logout(request)})
