from __future__ import unicode_literals

from django.contrib.auth import (login as auth_login,  authenticate)

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from Home.models import Kid

def index(request):
	_message = ''
	
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('adminpanel:panel'))		

	if request.method == 'POST':
		_username = request.POST['user']
		_password = request.POST['pass']
		user = authenticate(username=_username, password=_password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect(reverse('adminpanel:panel'))
			else:
				_message = ''
		else:
			_message = 'Connexion non valide, veuillez reessayer'
	context = {'message': _message}
	return render(request, 'adminpanel/index.html', context)

def panel(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('adminpanel:index'))

	students = Kid.objects.all()
	
	context = {'name': request.user.get_full_name(), 'students': students}
	return render(request, "adminpanel/adminpanel.html", context)
