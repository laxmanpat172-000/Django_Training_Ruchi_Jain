from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    s = "<h1>Welcome to AIDS  of Sistec college gandhi nagar bhopal</h1>"
    return HttpResponse(s)

def information(request):
    s = "<h1>Information about AIDS  - artificial intelligence of data science which is a branch of computer science  and the best of branches   </h1>"
    return HttpResponse(s)

# Create your views here.
