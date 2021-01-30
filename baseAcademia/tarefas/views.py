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









# Create your views here.
