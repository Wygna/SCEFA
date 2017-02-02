from django.forms import ModelForm,forms
from appalunos.models import Aluno
from django import forms


class AlunoForm(ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Aluno
        fields = ('nome', 'email', 'turno_aula', 'matricula','senha')
