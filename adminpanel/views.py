from __future__ import unicode_literals

from django.contrib.auth import (login as auth_login,  authenticate)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def details(request, kid_id):
	kid = get_object_or_404(Kid, id=kid_id)
	if request.method == 'POST':
		if 'submit' in request.POST:
			for name in kid.kid_field_names:
				request_text = request.POST.get(name, None)
				if request_text is not None and request_text is not '':
					setattr(kid, name, request_text)
			kid.save()
			return HttpResponseRedirect('/adminpanel')
			
	return render(request, 'adminpanel/details.html', {'kid' : kid})

def panel(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('adminpanel:index'))

	students = Kid.objects.all()
	#if request.method == 'POST':		
	#	if 'add_kid' in request.POST:
			#print("neww kid")
			#new_kid = Kid()
			#new_kid.save()
	#		return HttpResponseRedirect('/pafnel/')# + str(new_kid.id))
	context = {'name': request.user.get_full_name(), 'students': students}
	return render(request, "adminpanel/adminpanel.html", context)
