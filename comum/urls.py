from django.conf.urls import url

from comum import views

urlpatterns = [
    url(r'^$', views.index),
]
