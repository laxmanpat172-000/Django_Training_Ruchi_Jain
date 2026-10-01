from django.urls import path
from CS import views as v2
urlpatterns = [
    path('home2/', v2.about),
    path('information2/', v2.information),
]   