from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.Base),
    path('', views.rotinaTreinos, name='rotina-Treinos')

]
