from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^authenticate/$', views.authenticate, name='authenticate'),
    url(r'^logout/$', views.login, name='logout'),
]
