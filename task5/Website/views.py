from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'city.html')

def information(request):
    return render(request, 'laptop.html')