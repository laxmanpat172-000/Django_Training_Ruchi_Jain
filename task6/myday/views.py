from django.shortcuts import render
from django.http import HttpResponse
from myday.models import product

def saveuser(request):# create record ( c for curd)
    p_id=104
    p_name="arnav"
    p_price= 212323
    p_offer= 76
    prd=product(p_price=p_price,p_name=p_name,p_id=p_id,p_offer=p_offer)
    prd.save()
    return HttpResponse("<h1> product delails save sucessfully </h1>") 

def saveuser2(request):
    p_id=111
    p_name="dakku"
    p_price= 50
    p_offer= 45
    prd=product(p_price=p_price,p_name=p_name,p_id=p_id,p_offer=p_offer)
    prd.save()
    return HttpResponse("<h1> product sucessfully ")
    
    p_id=105
    p_name="dal"
    p_price= 105
    p_offer= 96
    prd=product(p_price=p_price,p_name=p_name,p_id=p_id,p_offer=p_offer)
    prd.save()
    return HttpResponse("<h1> product sucessfully ")

def saveuser3(request):
    p_id=106
    p_name="daliya"
    p_price= 50
    p_offer= 45
    prd=product(p_price=p_price,p_name=p_name,p_id=p_id,p_offer=p_offer)
    prd.save()
    return HttpResponse("<h1> product sucessfully ")

def saveuser4(request):
    p_id=106
    p_name="chana"
    p_price= 105
    p_offer= 96
    prd=product(p_price=p_price,p_name=p_name,p_id=p_id,p_offer=p_offer)
    prd.save()
    return HttpResponse("<h1> product sucessfully ")

def saveuser5(request):
    p_id=107
    p_name="kurkure"
    p_price= 20
    p_offer= 18
    prd=product(p_price=p_price,p_name=p_name,p_id=p_id,p_offer=p_offer)
    prd.save()
    return HttpResponse("<h1> product sucessfully ")

def saveuser6(request):
    p_id=108
    p_name="meggi"
    p_price= 105
    p_offer= 90
    prd=product(p_price=p_price,p_name=p_name,p_id=p_id,p_offer=p_offer)
    prd.save()
    return HttpResponse("<h1> product sucessfully ")

def saveuser7(request):
    p_id=109
    p_name="menda"
    p_price= 40
    p_offer= 36
    prd=product(p_price=p_price,p_name=p_name,p_id=p_id,p_offer=p_offer)
    prd.save()
    return HttpResponse("<h1> product sucessfully ")

def saveuser8(request):
    p_id=110
    p_name="mugfali"
    p_price= 100
    p_offer= 65
    prd=product(p_price=p_price,p_name=p_name,p_id=p_id,p_offer=p_offer)
    prd.save()
    return HttpResponse("<h1> product sucessfully ")

# Create your views here.
