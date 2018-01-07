from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>[0-9]+)/$', views.show),
    url(r'^(?P<number>[0-9]+)/edit/$', views.edit),
    url(r'^(?P<number>[0-9]+)/delete/$', views.delete)
]
