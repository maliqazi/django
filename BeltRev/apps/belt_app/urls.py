from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books),
    url(r'^books/add$', views.addbook),
    url(r'^books/enterbook$', views.enterbook),
    url(r'^books/(?P<number>[0-9]+)/$', views.addreview),
    url(r'^books/(?P<number>[0-9]+)/enterreview$', views.enterreview),
    url(r'^users/(?P<number>[0-9]+)/$', views.users)
]
