from django.urls import path
from Sistec import views as v2
urlpatterns = [
    path('home3/', v2.home),
    path('information3/', v2.information),
]
