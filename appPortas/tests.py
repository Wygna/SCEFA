from appPortas.models import *
from appPonto.models import *

porta = Porta.objects.get(id=2)
grupoportas = GrupoPorta.objects.filter(porta=porta)
for grupoporta in grupoportas:
    for pessoa in grupoporta.grupo.grupopessoa_set.all():
        print(pessoa.pessoa)
