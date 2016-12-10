from django.forms import ModelForm
from alunos.models import Aluno


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ('nome', 'email', 'turno_aula', 'matricula')
