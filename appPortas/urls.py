from django.conf.urls import url
from django.contrib.auth.views import login,logout

from appPortas.views import *

urlpatterns = [
    url(r'^porta/list$', porta_list, name='porta_list'),
    url(r'^porta/detail/(?P<pk>\d+)$',
        porta_detail, name='porta_detail'),
    url(r'^porta/new/$', porta_new, name='porta_new'),
    url(r'^porta/update/(?P<pk>\d+)$',
        porta_update, name='porta_update'),
    url(r'^porta/delete/(?P<pk>\d+)$',
        porta_delete, name='porta_delete'),

]
