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
from django.conf.urls import url, include
from django.contrib import admin

from websaver.views import HomeView

#from bookmark.views import BookmarkLV, BookmarkDV


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include(('bookmark.urls','bookmark'), namespace='bookmark')),
    url(r'^blog/', include(('blog.urls', 'blog'), namespace='blog')),

    # url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    # url(r'^blog/', include('blog.urls', namespace='blog')),

    # class-based views for bookmark app
    # url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    # url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]
