from appPortas.models import *
from appPonto.models import *
from datetime import datetime

hora = datetime.now()
frequencia = Frequencia.objects.get(pessoa__id_digital=32, data=datetime.now().date())
print(frequencia)
