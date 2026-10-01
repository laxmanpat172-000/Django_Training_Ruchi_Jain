from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def textpaper(request):
    
    que="what is the jinja template?"
    a="Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates."
    b="It is fast, widely used and secure with the optional sandboxed template execution environment."
    c="Jinja is a template engine for the Python programming language. It is used to create dynamic web pages by allowing developers to embed Python code within HTML templates."
    d="Jinja is a template engine for Python. It is used to create dynamic web pages by allowing developers to embed Python code within HTML templates. It is designed to be fast, secure, and easy to use, and is often used in web frameworks such as Flask and Django."
    context={'que':que,'a':a,'b':b,'c':c,'d':d}
    template=loader.get_template('textpaper.html')
    rex=template.render(context,request)
    return HttpResponse(rex)

def name(request):
    Name="Name=Laxman patel"
    Department="Department=Computer Engineering"
    Age="Age=21"
    context={'Name':Name,'Department':Department,'Age':Age}
    template=loader.get_template('name.html')
    rex=template.render(context,request)
    return HttpResponse(rex)
def sum(request):
    a="a=10"
    b="b=20"
    c="sum=30"
    context={'a':a,'b':b,'c':c}
    template=loader.get_template('sum.html')
    rex=template.render(context,request)
    return HttpResponse(rex)

def result(request):
    """ye upr ki  three line vale code ko hun ne 1 line me likh hain iska matlab ye hain ki humne 3 variable ko 1 line me likh diya hain aur usko context me pass kar diya hain"""
    context={'name':"laxman",
             'marks':90}
    return render(request,'result.html',context)

def voting(request):
    context={'name':"laxman",
             'age':21}
    return render(request,'voting.html',context)

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
