from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path("load",views.load,name="load"),
    path("load1",views.load1,name="load1"),
    path("prints",views.prints,name="prints"),
    path("Avg_max",views.Avg_max,name="Avg_max"),
    path("Avg_min",views.Avg_min,name="Avg_min"),
    path("Sum_pre",views.Sum_pre,name="Sum_pre"),
    
]
