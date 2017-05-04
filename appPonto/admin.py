from django.contrib import admin
from appPonto.models import *
# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Frequencia_funcionario)
admin.site.register(Dias_sem_expediente)
