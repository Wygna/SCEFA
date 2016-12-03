from django.forms import ModelForm
from appPonto.models import *

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome','matricula','telefone')

class AdministradorForm(ModelForm):
    class Meta:
        model = Administrador
        fields = ('nome','matricula','telefone')