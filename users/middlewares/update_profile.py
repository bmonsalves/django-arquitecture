from django.shortcuts import redirect
from django.urls import reverse


class UpdateProfileMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user = request.user
        if not user.is_anonymous:
            profile = user.profile

            if not profile:
                return redirect('user_login')

            if not profile.picture or not profile.biography:
                if request.path not in (reverse('user_profile'), reverse('user_logout')):
                    return redirect('user_profile')

        return self.get_response(request)
