from django.contrib import admin
from appPortas.models import *

# Register your models here.
admin.site.register(Grupo)
admin.site.register(Porta)
admin.site.register(Usuario)
admin.site.register(Porta_Grupo)
admin.site.register(Usuario_Grupo)
admin.site.register(Registro_porta)
