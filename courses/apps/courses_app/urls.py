from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^courses/$', views.index),
    url(r'^courses/add/$', views.add),
    url(r'^courses/destroy/(?P<number>[0-9]+)$', views.destroy),
    url(r'^courses/delete_course/(?P<number>[0-9]+)$', views.delete_course)
]
