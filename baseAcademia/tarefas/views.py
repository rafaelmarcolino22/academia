from django.shortcuts import render, get_object_or_404, redirect
from .  models import alunoTreino
from . forms import TreinoNov

def rotinaTreinos(request):
    exerc = alunoTreino.objects.all
    return render(request, 'rotina.html', {'exerc':exerc})   








def novoTreino(request):
    if request.method == 'POST':

        form = TreinoNov(request.POST)

        if form.is_valid():
            exerc =  form.save(commit=False)
            exerc.done = 'doing'
            exerc.save()
            return redirect('/')

    else:
        
        form = TreinoNov()

    return render(request, 'novotreino.html', {'form':form})






    return render(request, 'novotreino.html', {'forms': forms})    



# Create your views here.
