"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login_view/',views.login_view,name='login'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_view,name='profile'),
    path('send_otp/',views.send_otp,name='send_otp'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('reset_password/',views.reset_password,name='reset_password'),
]
