from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
 

def shopping(request):
    template=loader.get_template('shopping.html')
    return HttpResponse(template.render())
    
# Create your views here.
