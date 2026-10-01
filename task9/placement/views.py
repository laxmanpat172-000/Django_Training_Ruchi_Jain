from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from placement.models import Registraion
from django.urls import reverse 
import joblib


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def signup(request):
    return render(request, 'signup.html')


def prediect(request):
    return render(request, 'prediect.html')


def result(request):

    scaler = joblib.load('scalermodel (1).pkl')
    mlmodel = joblib.load('mlmodel (1).pkl')

    cgpa = float(request.GET['cgpa'])
    iq = float(request.GET['iq'])
    profile_score = float(request.GET['profile_score'])

    data = [cgpa, iq, profile_score]

    scaler_input = scaler.transform([data])

    ans = mlmodel.predict(scaler_input)[0]

    return render(
        request,
        'result.html',
        {
            'Answer': ans,
            'cgpa': cgpa,
            'iq': iq,
            'profile_score': profile_score
        }
    )
# def result(request):
#     scaler=joblib.load('scalermodel.pkl')
#     mlmodel=joblib.load('mlmodel.pkl')
#     cgpa=float(request.GET['cgpa'])
#     iq=float(request.GET['iq'])
#     profile_score=float(request.GET['profile_score'])
#     data=[cgpa,iq,profile_score]
#     scaler_input=scaler.transform([data])
#     ans=int(mlmodel.predict(scaler_input)[0])
#     return render(request,'result.html',{'Answer':ans,'CGPA':cgpa,'Profile_score':profile_score,'iq':iq})