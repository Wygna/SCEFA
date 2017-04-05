from django.contrib.auth.models import Group
from appPonto.models import *

funcionario = Funcionario.objects.get(id=6)
grupoFuncionario = Group.objects.get(name='funcionario')
grupoFuncionario.user_set.add(funcionario)

