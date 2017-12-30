from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^users$', views.index),     # This line has changed!
    url(r'^users/new/$', views.new),
    url(r'^users/create/$', views.create),
    url(r'^users/update/$', views.update),
    url(r'^users/(?P<number>[0-9]+)/$', views.show),
    url(r'^users/(?P<number>[0-9]+)/edit$', views.edit),
    url(r'^users/(?P<number>[0-9]+)/destroy$', views.destroy)
]
