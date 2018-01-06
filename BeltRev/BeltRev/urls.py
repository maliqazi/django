"""BeltRev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.belt_app.urls')),
    url(r'^add', include('apps.belt_app.urls')),
    url(r'^login$', include('apps.belt_app.urls')),
    url(r'^logout$', include('apps.belt_app.urls')),
    url(r'^books$', include('apps.belt_app.urls')),
    url(r'^books/add$', include('apps.belt_app.urls')),
    url(r'^books/enterbook$', include('apps.belt_app.urls')),
    url(r'^books/(?P<number>[0-9]+)/$', include('apps.belt_app.urls')),
    url(r'^books/(?P<number>[0-9]+)/enterreview$', include('apps.belt_app.urls')),
    url(r'^users/(?P<number>[0-9]+)/$', include('apps.belt_app.urls'))
]
