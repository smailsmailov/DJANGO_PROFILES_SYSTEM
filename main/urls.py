from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('',  home_page , name = 'home') ,
]

# PATERNS ACCOUNT REWRITED

urlpatterns += [
    path('accounts/registration/',  registration_page , name = 'home') ,
    path('accounts/login/',  login_page , name = 'login') ,
    path('accounts/profile_page/',  profile_page , name = 'profile') ,
    path('accounts/logout/',  logout , name = 'logout') ,
]

