from django.contrib.auth.models import Permission
from appPonto.models import *

frequencia_pessoa = Frequencia.objects.get(id=264)
frequencia_pessoa.delete()
