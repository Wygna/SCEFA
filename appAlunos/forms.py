from django.forms import ModelForm, forms
from appAlunos.models import Aluno
from django import forms


class AlunoForm(ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput, required=False)
    class Meta:
        model = Aluno
        fields = (
        'nome', 'matricula', 'cpf', 'dataNascimento', 'sexo', 'endereco', 'telefone', 'Email', 'turno_aula', 'foto',
        'situacao', 'senha')
