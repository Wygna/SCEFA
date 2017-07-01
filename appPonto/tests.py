from django.contrib.auth.models import Permission
from appPonto.models import *

frequencia_pessoa = Frequencia.objects.get(id=991)
print(frequencia_pessoa)
