from django.urls import path
from .views import *
from .views import result

urlpatterns = [

    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('registration/', registration, name='registration'),
    path('prediect/', prediect, name='prediect'),
    path('result/', result, name='result'),

]