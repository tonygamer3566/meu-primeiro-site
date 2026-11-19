from django import forms
from .models import projeto

class projetoForm(forms.ModelForm):
    class Meta:
        model = projeto
        fields = ['nome', 'ano', 'descricao', 'categoria']
                  