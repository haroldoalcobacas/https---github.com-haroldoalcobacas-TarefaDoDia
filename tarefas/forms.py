

from django import forms
from .models import Tarefa

class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('descricao', 'categoria')

class EditarTarefa(forms.Form):
    Opcoes_Categoria = (
        ('urgente','Urgente'),
        ('importante', 'Importante'),
        ('comum', 'Comum'),
    )

    tarefa = forms.CharField(max_length=400)
    categoria = forms.ChoiceField(choices=Opcoes_Categoria)