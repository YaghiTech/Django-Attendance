from django.conf.urls import url

from . import views
from django.contrib.auth.views import logout

app_name = 'adminpanel'


urlpatterns = [
    url(r'login', views.index, name='index'),
	url(r'^logout/$', logout, {'next_page': "/"}, name='logout'),
	url(r'panel', views.panel, name='panel'),
]
