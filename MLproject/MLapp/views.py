from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib


def home(request):
    return render(request, 'home.html')


def result(request):
    scaler = joblib.load('scalermodel.pkl')
    mlmodel = joblib.load('mlmodel.pkl')

    list = []

    list.append(request.GET['RI'])
    list.append(request.GET['Na'])
    list.append(request.GET['Mg'])
    list.append(request.GET['Al'])
    list.append(request.GET['Si'])
    list.append(request.GET['K'])
    list.append(request.GET['Ca'])
    list.append(request.GET['Ba'])
    list.append(request.GET['Fe'])

    scaler_input = scaler.transform([list])

    ans = mlmodel.predict(scaler_input)[0]

    return render(
        request,
        'result.html',
        {
            'Answer': ans,
            'list': list
        }
    )