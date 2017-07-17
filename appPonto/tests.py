from django.contrib.auth.models import Permission
from appPonto.models import *

frequencia = Frequencia.objects.filter(~Q(hora_saida=None), pessoa_id=7)
for e in frequencia:
    if e.tempoMaximo() == 1:
        print('alo')


        #            if tempo[1] != ':':
        # tempo_maximo = datetime.time(int(tempo[0]),int(tempo[2:4],int(tempo[5:])))
