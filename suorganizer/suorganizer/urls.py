"""suorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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


#from organizer import urls as organizer_urls

from blog import urls as blog_urls

from contact import urls as contact_urls

##from organizer.views import tag_detail

##from blog.views import PostList

from .views import redirect_root

from organizer.urls import (newslink as newslink_urls,
    startup as startup_urls, tag as tag_urls)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^helloworld/$', greeting),
    #url(r'^startupDetail/$', startupDetail),
    #url(r'^startupList/$', startupList),

    #url(r'^', include(organizer_urls)),

    url(r'^blog/', include(blog_urls)), 

    url(r'^contact/', include(contact_urls)),


    url(r'^newslink/', include(newslink_urls)),
    url(r'^startup/', include(startup_urls)),
    url(r'^tag/', include(tag_urls)),


    #url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),


    #url(r'^tag_form/$', tag_form, name='organizer_tag_create'),


    #url(r'^$', include(blog_urls)),

    url(r'^$', redirect_root),

]












