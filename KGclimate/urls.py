from django.conf.urls import patterns, url

from KGclimate import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)