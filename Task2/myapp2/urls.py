from django.urls import path
from myapp2 import views
from django.contrib import admin

urlpatterns = [
    path('sistec/', views.sistec),
    path('admin/', admin.site.urls),

]