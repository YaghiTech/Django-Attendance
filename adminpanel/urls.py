from django.conf.urls import url

from . import views
from django.contrib.auth.views import logout

app_name = 'adminpanel'


urlpatterns = [
    url(r'login', views.index, name='index'),
	url(r'^logout/$', logout, {'next_page': "/"}, name='logout'),
	url(r'panel/$', views.panel, name='panel'),
	url(r'panel/(?P<kid_id>[0-9]+)/$', views.details, name='detail'),
	url(r'panel/add_kid/$', views.add_kid, name='add_kid')
]
