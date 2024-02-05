

from django import forms
from .models import Tarefa

class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao', 'categoria', 'prazo' ]
        labels = {
            'descricao': 'Descrição',
            'categoria': 'Categoria',
            'prazo': 'Prazo',  
        }
        widgets = {'prazo': forms.DateTimeInput(attrs={'type': 'date' }),
        }

class EditarTarefa(forms.Form):
    
        Opcoes_Categoria = (
            ('urgente','Urgente'),
            ('importante', 'Importante'),
            ('comum', 'Comum'),
        )

        descrição = forms.CharField(max_length=400)
        categoria = forms.ChoiceField(choices=Opcoes_Categoria)
        widgets = {'conclusao': forms.DateTimeInput(attrs={'type': 'date' }),
            }



   
        