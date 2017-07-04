from appPonto.models import *
from appPortas.models import *
from datetime import datetime

frequencia = Frequencia.objects.get(pessoa__id_digital=1, data=datetime.now().date())
hora = datetime.now()
frequencia.hora_saida = hora.strftime("%H:%M:%S")
frequencia.hora_saida
frequencia.save()
