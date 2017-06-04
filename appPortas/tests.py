from django.test import TestCase
from appPonto.models import *
departamento = Departamento.objects.get(id=1)
cargo  = Cargo.objects.get(id=1)
cargo_departmento = Cargo.objects.filter(departamento=departamento)
cargo.departamento_id = 0
cargo.save()
print(cargo)