from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^midia/', include('midia.urls')),
    url(r'^comum/', include('comum.urls')),
    url(r'^admin/', admin.site.urls),
]
