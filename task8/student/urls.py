from django.urls import path
from .views import *

urlpatterns = [

    path('home/', home, name='home'),

    path('signup/',signup, name='signup'),

    path('saveuser/', saveuser, name='saveuser'),

    path('login/', login, name='login'),

    path('loginvalidation/', loginvalidation, name='loginvalidation'),
    
    path('student_registration/',student_registration,name='student_registration'),


]