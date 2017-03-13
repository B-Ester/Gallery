from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name= 'about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$' , article, name='article'),
    url(r'^articles/addlike/(?P<article_id>[0-9]+)/$', addlike , name='addlike'),
    url(r'^upload/$', upload)

    ]

