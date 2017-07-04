from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('appPonto.urls')),
    url(r'', include('appAlunos.urls')),
    url(r'', include('appPortas.urls')),
]
urlpatterns += staticfiles_urlpatterns()
