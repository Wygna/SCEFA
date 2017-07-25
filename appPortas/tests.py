from appPortas.models import *
from appPonto.models import *
from datetime import datetime

pessoa = Pessoa.objects.get(id)
print(pessoa)
