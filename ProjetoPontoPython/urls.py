
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('appPonto.urls')),
    url(r'', include('appalunos.urls')),
    url(r'', include('appPortas.urls')),
]
