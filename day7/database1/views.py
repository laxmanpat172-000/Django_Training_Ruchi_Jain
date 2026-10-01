from django.shortcuts import render
from django.http import HttpResponse
from database1.models import Employee

# Create your views here.
def saveuser(request):# create record ( c for curd)
    E_no=105
    E_name="arnav"
    E_sal=45456
    E_mp=Employee(E_no=E_no,E_name=E_name,E_sal=E_sal)
    E_mp.save()
    return HttpResponse("<h1> user save sucessfully </h1>") 
    
def employeelist(request): # read data recodes( R for curd)
    Employees=Employee.objects.all() # it return employee
    res=render(request,'employeelist.html',{'Employees':Employees})
    return res 
    
def updateemployee(request):
    id=5
    E_no=105
    E_name="vijay"
    E_sal=87689
    Employee(id=id,E_name=E_name,E_no=E_no,E_sal=E_sal).save()
    return HttpResponse("<h1> update sucessfully</h>")


def update(request):
    id=3
    E_no=103
    E_name="vijay"
    E_sal=87689
    Employee(id=id,E_name=E_name,E_no=E_no,E_sal=E_sal).save()
    return HttpResponse("<h1> update sucessfully</h>")


    
def deleteemployee(request):
    id=104
    emp=Employee.objects.filter(id=id)
    emp.delete()
    return HttpResponse("<h1> delete record sucessfully</h>")
    
    