from django.urls import path
from . views import *

urlpatterns = [
    path('saveuser/',saveuser),
    path('employeelist/',employeelist),
    path('updateemployee/',updateemployee),
    path('update/',update),
    path('deleteemployee/',deleteemployee),
    
]

