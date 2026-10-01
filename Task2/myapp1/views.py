from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def textpaper(request):
    template=loader.get_template('textpaper.html')
    return HttpResponse(template.render())
# Create your views here