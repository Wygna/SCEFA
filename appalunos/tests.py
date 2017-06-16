from django.test import TestCase

from appalunos.models import *


aluno = Aluno.objects.get(id=7)
print(aluno)
