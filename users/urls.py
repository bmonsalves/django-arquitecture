"""testgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView

from .views.login import login
from .views.logout import logout
from .views.signup import signup
from .views.profile import update, index

urlpatterns = [
    path('login/', login.login_view, name='user_login'),
    path('login/json/', login.login_json, name='user_login_json'),

    path('logout/', logout.logout_view, name='user_logout'),
    path('logout/json/', logout.logout_json, name='user_logout_json'),

    path('signup/', signup.signup, name='user_signup'),
    path('signup/json/', signup.signup_json, name='user_signup_json'),

    path('profile/', update.update, name='user_profile'),
    path('profile/json', update.update_json, name='user_profile_json'),

    path(route='profile/detail/<str:username>/',
         view=index.Index.as_view(template_name='detail.html'),
         name='contact_profile'),

    path(route='profile/detail/<str username>/json',
         view=index.Index.as_view(template_name='detail.html'),
         name='contact_profile'),

]
