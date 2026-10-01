from django.shortcuts import render
from django.http import HttpResponse

def facebook(request):
    s = "<h1>Welcome to Facebook</h1>"
    return HttpResponse(s)

def instagram(request):
    s = "<h1>Welcome to Instagram</h1>"
    return HttpResponse(s)


# Create your views here.
