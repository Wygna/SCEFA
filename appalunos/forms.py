from django.forms import ModelForm, forms
from appAlunos.models import Aluno
from django import forms


class AlunoForm(ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Aluno
        fields = ('nome', 'email', 'turno_aula', 'matricula', 'foto', 'telefone', 'senha')
