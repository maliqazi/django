"""main URL Configuration

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
    #url(r'^', include('apps.first_app.urls')),
    url(r'^', include('apps.blogs_app.urls')),
    url(r'^new$', include('apps.blogs_app.urls')),
    url(r'^create$', include('apps.blogs_app.urls')),
    url(r'^(?P<number>[0-9]+)/$', include('apps.blogs_app.urls')),
    url(r'^(?P<number>[0-9]+)/edit/$', include('apps.blogs_app.urls')),
    url(r'^(?P<number>[0-9]+)/delete/$', include('apps.blogs_app.urls'))
    #url(r'^', include('apps.timeDisplay.urls'))
    #url(r'^', include('apps.randomWord.urls')),
    #url(r'^gen$', include('apps.randomWord.urls')),
    #url(r'^reset$', include('apps.randomWord.urls'))
]
