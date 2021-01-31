from django.shortcuts import render, get_object_or_404, redirect
from .models import alunoTreino
from .forms import TreinoNov

def rotinaTreinos(request):
    exerc = alunoTreino.objects.all
    return render(request, 'rotina.html', {'exerc':exerc})   


def novoTreino(request):
    if request.method == 'POST':

        forms = TreinoNov(request.POST)

        if forms.is_valid():
            exerc =  forms.save(commit=False)
            exerc.done = 'doing'
            exerc.save()
            return redirect('/')

    else:
        
        forms = TreinoNov()

    return render(request, 'novotreino.html', {'forms':forms})


def editarExerc(request):    
    exerc = alunoTreino.objects.all

    return render(request, 'editar.html', {'exerc':exerc})


def edicao(request, id):
    exerc = get_object_or_404(alunoTreino, pk=id)
    forms = alunoTreino(instance=exerc)

    if(request.method == 'POST'):
        forms = alunoTreino(request.POST, instance=exerc)

        if(request.method == 'POST'):
            forms = alunoTreino(request.POST, instance=exerc)

            if(forms.is_valid()):
                exerc.save()
                return render(request, 'edicao.html', {'exerc':exerc, 'forms':forms})


    return render(request, 'edicao.html', {'exerc':exerc, 'forms':forms})







# Create your views here.
