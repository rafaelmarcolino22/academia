from django.shortcuts import render, get_object_or_404, redirect
from .models import alunoTreino
from .forms import TreinoNov

def rotinaTreinos(request):
    exercs = alunoTreino.objects.all
    return render(request, 'rotina.html', {'exercs':exercs})   


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
    exercs = alunoTreino.objects.all

    return render(request, 'editar.html', {'exercs':exercs})


def edicao(request, id):
    exerc = get_object_or_404(alunoTreino, pk=id)
    forms = TreinoNov(instance=exerc)

    if(request.method == 'POST'):
        
        forms = TreinoNov(request.POST, instance=exerc)

        if(request.method == 'POST'):
            forms = TreinoNov(request.POST, instance=exerc)

            if(forms.is_valid()):
                exerc.save()
                return redirect('/')
            else:

                return render(request, 'edicao.html', {'exerc':exerc, 'forms':forms })
    else:
        return render(request, 'edicao.html', {'exerc':exerc, 'forms':forms })


# Create your views here.
