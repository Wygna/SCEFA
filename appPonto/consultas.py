from appPonto.models import *
from appPortas.models import *

pessoa = Pessoa.objects.get(id=5)
print(pessoa)
