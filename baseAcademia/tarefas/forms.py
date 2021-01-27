from django import forms
from . models import alunoTreino

class TreinoNov(forms.ModelForm):

    class Meta:
        model = alunoTreino
        fields = ('exercicio', 'repeticao')
