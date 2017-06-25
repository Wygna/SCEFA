from appPonto.models import *
from appPortas.models import Porta

portas = Porta.objects.all()
for e in portas:
    print(e.local)
