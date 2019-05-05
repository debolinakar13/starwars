from django.conf.urls import url

from . import views

urlpatterns = [
    url('^search/(?P<title>.+)/$', views.search_planet, name='search'),
    url('^list-planet', views.list_planet, name='planet'),
    url('^list-films', views.list_film, name='film')
]
