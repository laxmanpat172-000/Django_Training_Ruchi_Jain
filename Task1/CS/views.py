from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    s= "<h1>Welcome to CS  of Sistec college gandhi nagar bhopal is a great place to learn and grow</h1>"
    return HttpResponse(s)

def information(request):
    s= "<h1>Information about CS  - computer science is a branch of computer science  and the best of branches   </h1>"
    return HttpResponse(s)

# Create your views here.
