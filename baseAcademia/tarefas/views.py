from django.shortcuts import render, get_object_or_404
from .  models import alunoTreino
from . forms import TreinoNov

def rotinaTreinos(request):
    exerc = alunoTreino.objects.all
    return render(request, 'rotina.html', {'exerc':exerc})   

def novoTreino(request):
    forms = TreinoNov()
    return render(request, 'novotreino.html', {'forms': forms})    



# Create your views here.
