from django.test import TestCase

from appPonto.models import *
funcionario = Funcionario.objects.get(id=1)
print(funcionario.nome)