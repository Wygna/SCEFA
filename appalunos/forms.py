from django.forms import ModelForm
from appalunos.models import Aluno


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ('nome', 'email', 'turno_aula', 'matricula')
