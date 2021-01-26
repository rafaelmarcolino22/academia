from django.shortcuts import render, get_object_or_404
from .  models import alunoTreino

def rotinaTreinos(request):
    exerc = alunoTreino.objects.all
    return render(request, 'rotina.html', {'exerc':exerc})   

def novoTreino(request):
    return render(request, 'novotreino.html')    



# Create your views here.
