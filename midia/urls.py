from django.conf.urls import url

from midia import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^atores/$', views.atores_list),
    url(r'^filmes/$', views.filmes_list),
    url(r'^diretores/$', views.diretores_list),
    url(r'^filme/(?P<id>\d+)/$', views.filme_detail),
]