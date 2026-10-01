from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    s = "<h1>Welcome to Django</h1>"
    return HttpResponse(s)


def about(request):
    s = "<h1> this is the About page </h1>"
    return HttpResponse(s)

# Create your views here.
