from appPonto.models import *
from appPortas.models import *

pessoa = Pessoa.objects.get(id=1)
print(pessoa)
