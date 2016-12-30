from django.forms import ModelForm,forms
from django import forms

from appPonto.models import *

class FuncionarioForm(ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Funcionario
        fields = ('nome','matricula','telefone','Email','senha')

class AdministradorForm(ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Administrador
        fields = ('nome', 'matricula', 'telefone', 'Email', 'senha')