from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^process_money/(?P<path>\w{0,10}$)', views.process),
    url(r'^reset', views.reset),
    url(r'^', views.index)
]