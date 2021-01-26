from django.shortcuts import render, get_object_or_404
from .  models import alunoTreino

def rotinaTreinos(request):
    exerc = alunoTreino.objects.all
    return render(request, 'rotina.html', {'exerc':exerc})   



# Create your views here.
