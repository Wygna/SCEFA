from django.forms import ModelForm, forms, DateInput
from appPonto.models import *
from django import forms

class FuncionarioForm(ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Funcionario
        fields = ('nome', 'matricula', 'telefone', 'cargo', 'Email', 'foto', 'situacao', 'senha')


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields  = ('descricao',)

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields  = ('nome_funcao','departamento')

class DataForm(forms.Form):
    data_inicial = forms.DateField("Data da inicial")
    class Meta:
        fields = ('data_inicial',)
        error_messages = {
            'data_inicial': {
                'invalid': 'Data de Venda Inválida',
                'required': 'Informe a Data da Venda'
            }
        }
        widgets = {
            'data_final': DateInput(attrs={'class': 'datepicker'}),

        }


class AddObservacaoFrequencia(forms.Form):
    observacao = forms.CharField(widget=forms.Textarea, label='Observação')
