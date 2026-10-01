from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from student.models import newuser,srs
from django.urls import reverse


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')


def saveuser(request):

    user1 = newuser()

    u = newuser.objects.filter(
        username=request.POST['username']
    )

    if not u:

        user1.username = request.POST['username']
        user1.password = request.POST['password']
        user1.name = request.POST['name']

        user1.save()

        return HttpResponseRedirect(reverse('login'))

    else:

        return render(
            request,
            'signup.html',
            {'errormessage': 'Username is Already Exists'}
        )


def login(request):
    return render(request, 'login.html')


def loginvalidation(request):

    try:

        user1 = newuser.objects.get(
            username=request.POST['username'],
            password=request.POST['password']
        )

        return HttpResponseRedirect(reverse('student_registration'))

    except newuser.DoesNotExist:

        return render(
            request,
            'login.html',
            {'erg': 'Invalid username or password'}
        )

def student_registration(request):

    if request.method == "POST":

        s_id = request.POST['s_id']
        s_name = request.POST['s_name']
        s_branch = request.POST['s_branch']

        student = srs(
            s_id=s_id,
            s_name=s_name,
            s_branch=s_branch
        )

        student.save()

        return render(request, 'Registration.html', {
            'message': 'Your record is saved successfully'
        })

    return render(request, 'Registration.html')