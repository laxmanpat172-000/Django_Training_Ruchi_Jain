from django.urls import path
from AIDS import views as v1
urlpatterns = [
    path('home1/', v1.home),
    path('information1/', v1.information),
]