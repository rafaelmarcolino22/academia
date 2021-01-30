from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.rotinaTreinos, name='rotina-Treinos'),
    path('oi/', views.novoTreino, name='novo-treino'),
    path('editar/', views.editarExerc, name='editar-exercicios')


]
