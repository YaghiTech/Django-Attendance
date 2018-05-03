from django.shortcuts import render, HttpResponseRedirect
from .models import Kid, Teacher, SignIn
import datetime
# Create your views here.
def index(request):
	all_kids = Kid.objects.all()
	name = ""

	if request.method == "POST":
		for kid in all_kids:
			
			if 'signout_'+str(kid.id) in request.POST:
				setattr(kid, 'kid_signed_in', False)
				kid.save()

				sign_in = SignIn.objects.get(kid_id=kid.id,currently_signed_in=True)
				setattr(sign_in, 'currently_signed_in', False)
				setattr(kid, 'time_left', datetime.datetime.now())
				sign_in.save()

				#new_sign_in = SignIn(kid=kid)
				#new_sign_in.kid = kid
				#new_sign_in.save()
				return HttpResponseRedirect('/')

		name = request.POST.get("name", None)
		grade =request.POST.get("grade", None)
		if grade is None:
			grade = " "
		if(name == 'delete_all'):
			Kid.objects.all().delete()
			SignIn.objects.all().delete()
			return HttpResponseRedirect('/')
		elif (len([x for x in all_kids if x.kid_name == name]) == 0):
			#newkid = Kid()
			#newkid.kid_name = name
			#newkid.kid_signed_in = True
			#newkid.save()
			return render(request, "Home/index.html", {'all_kids' : all_kids,
					 'kids_signed_in' : [x for x in SignIn.objects.all() if x.currently_signed_in == True], 'all_teachers' : Teacher.objects.all(),
					 'all_sign_ins' : SignIn.objects.all, 'kid_does_not_exist' : True})
			return HttpResponseRedirect('/')
		else:
			kid = Kid.objects.get(kid_name=name)
			setattr(kid, 'kid_signed_in', True)
			setattr(kid, 'time_entered', datetime.datetime.now())

			setattr(kid, 'subject',  request.POST.get("subject", None))
			setattr(kid, 'place',  request.POST.get("place", None))
			setattr(kid, 'reason', request.POST.get("reason", None))
			setattr(kid, 'teacher_name', request.POST.get("teacher", None))

			kid.save()

			new_sign_in = SignIn()
			new_sign_in.kid_name = kid.kid_name
			new_sign_in.kid_grade = kid.kid_grade
			new_sign_in.reason = request.POST.get("reason", None)
			new_sign_in.place = request.POST.get("place", None)
			new_sign_in.subject = request.POST.get("subject", None)
			new_sign_in.teacher_name =  request.POST.get("teacher", None)
			new_sign_in.time_entered = datetime.datetime.now()
			new_sign_in.kid_id = kid.id

			print(request.POST.get("place", None))
			#new_sign_in.time_left = datetime.datetime.now()

			new_sign_in.save()
		
			return HttpResponseRedirect('/')

		
		
	return render(request, "Home/index.html", {'all_kids' : all_kids,
					 'kids_signed_in' : [x for x in SignIn.objects.all() if x.currently_signed_in == True], 'all_teachers' : Teacher.objects.all(),
					 'all_sign_ins' : SignIn.objects.all, "kid_does_not_exist" : False})


def adminlogin(request):
	return render(request, "Home/adminlogin.html")
