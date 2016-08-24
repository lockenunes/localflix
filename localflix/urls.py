from django.conf.urls import url, include
from django.contrib import admin

from localflix import views

urlpatterns = [
    url(r'^comum/', include('comum.urls')),
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
]
