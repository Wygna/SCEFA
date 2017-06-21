from django.contrib.auth.models import Permission

from appPonto.models import *
#can_fm_list = Permission.objects.all()
#for e in can_fm_list:
 #   print(e.name)


funcionario =  Pessoa.objects.get(username__exact=225)
print(funcionario)

#from tastypie.models import ApiKey
#ApiKey.objects.create(key='1a23', user=funcionario)