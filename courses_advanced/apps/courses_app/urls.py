from django.conf.urls import url
from . import views

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^logout$', views.logout),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/update$', views.update),
    url(r'^(?P<id>\d+)/show$', views.show),
    url(r'^(?P<id>\d+)/join$', views.join),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
]