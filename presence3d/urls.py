from django.conf.urls import patterns, url
from presence3d import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
