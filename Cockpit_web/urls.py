"""Cockpit_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from account.views import topviews,greeting,testing,addmessage #import the app from account folder  
from Home.views import homeviews #import the app from Home folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',topviews),            #when the account/ called upon, run the topview function
    path('login_with_error/',topviews), #topview with error code 1
    path('home/',homeviews),
    path('',homeviews),           #the landing page 
    path('addmessage/',addmessage),     #data interupt function 
    path('greeting/',greeting),         
    path('testing/',testing) #for testing coding and development, delete before deploy.
]
