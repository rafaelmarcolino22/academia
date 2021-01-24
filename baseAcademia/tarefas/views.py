from django.shortcuts import render

def Base(request):
    return render(request, 'base.html')

def rotinaTreinos(request):
    
    return render(request, 'rotina.html')    

# Create your views here.
