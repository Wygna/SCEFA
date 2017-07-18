from appPortas.models import *
from appPonto.models import *

grupopessoa = GrupoPessoa.objects.filter(pessoa__id_digital=2)
grupoporta = GrupoPorta.objects.filter(porta_id=2)
for grupo in grupopessoa:
    for porta in grupoporta:
        if grupo.grupo == porta.grupo:
            print('22')
