from django.urls import path
from .views import *

urlpatterns=[

    path('home/',home,name='Home'),
    path('Signup/',Signup,name='Signup'),
    path('saveuser/',saveuser,name='saveuser'),
    path('login/',login,name='login'),
    path('loginvalidation/',loginvalidation,name='loginvalidation'),
    path('logout/',logout,name='logout'),


]