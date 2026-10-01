from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    s = "<h1>Welcome to Sistec College</h1>"
    return HttpResponse(s)

def information(request):
    s = "<h1>Information about Sistec College - Sistec College is a great place to learn and grow</h1>"
    return HttpResponse(s)


# Create your views here.
