from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from account.models import register #import the class from the models in the app

# Create your views here.

def homeviews(request):
    return render(request, 'Home/home.html') #django is going to look for html in the folder

# def goreg(request):
    