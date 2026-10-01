from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myuser.models import user
from django.urls import reverse


# Home
def home(request):
    return render(request, 'home.html')


# Signup page
def Signup(request):
    return render(request, 'Signup.html')


# Save user
def saveuser(request):

    user1 = user()

    u = user.objects.filter(username=request.POST['username'])

    if not u:

        user1.username = request.POST['username']
        user1.password = request.POST['password']
        user1.name = request.POST['name']
        user1.contact = request.POST['contact']

        user1.save()

        return HttpResponseRedirect(reverse('login'))

    else:

        return render(
            request,
            'Signup.html',
            {'errormsg': 'Username Already Exist'}
        )


# Login page
def login(request):
    return render(request, 'login.html')


def loginvalidation(request):

    try:

        user1 = user.objects.get(
            username=request.POST['username'],
            Pass=request.POST['password']
        )
        # session crete
        request.session['username']=user1.username
        request.session['name']=user1.name
        return HttpResponseRedirect(reverse('Home'))

    except user.DoesNotExist:

        return render(
            request,
            'login.html',
            {'errormsg': 'Invalid username or password'}
        )
# Logout
def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse( 'login'))