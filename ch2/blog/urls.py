"""websaver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
from django.conf.urls import url
from blog.views import *


urlpatterns = [

    # class-based views for blog app
    url(r'^$',PostLV.as_view(), name='index'),
    # example /post/
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    #/post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    #/archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    #/2012/
    url(r'^(?P<year>\d{4})/$',PostYAV.as_view(), name='post_year_archive'),
    #/2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',PostMAV.as_view(),\
                                                 name='post_month_archive'),
    # /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$',PostDAV.as_view(), \
                                                 name='post_day_archive'),
    #/today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

]
