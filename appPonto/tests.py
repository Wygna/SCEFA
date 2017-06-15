from django.contrib.auth.models import Permission

from appPonto.models import *
can_fm_list = Permission.objects.all()
for e in can_fm_list:
    print(e.name)
