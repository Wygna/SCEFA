from django.test import TestCase

from appPonto.models import *
#for f in Funcionario.objects.filter(id=10):
 #   for e in f.registrarponto_set.all():
  #      print(e.entrada)
for e in Funcionario.objects.all():
    print(e)