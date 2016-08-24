from django.conf.urls import url

from midia import views

urlpatterns = [
    url(r'^filme/(?P<id>\d+)/$', views.filme_detail),
]