from django.contrib.auth.models import Permission
from appPonto.models import *

frequencia_pessoa = Frequencia.objects.filter(hora_entrada__isnull=None)

print(frequencia_pessoa)
