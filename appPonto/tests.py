from django.db.models import Q

from appPonto.models import *
from appPonto.funcoes import *


funcionario = Funcionario.objects.get(id=2)
frequencias = funcionario.frequencia_set.filter(~Q(hora_entrada=None),~Q(data__week_day=7), ~Q(data__week_day=1),
                                                data__gte='2017-05-01',data__lte='2017-05-02').order_by('data')

s = '08:12:23'
t = '19:14:23'
f = '%H:%M:%S'
#dif = (datetime.strptime(t, f) - datetime.strptime(s, f))
#dif2 = (datetime.strptime(t, f) - datetime.strptime(s, f))
print(tempo_total(frequencias))