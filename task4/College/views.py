from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def sistec(request):
    return render(request, 'sistec.html')


def lnct(request):
    return render(request, 'lnct.html')


def nri(request):
    return render(request, 'nri.html')