from django.shortcuts import render, HttpResponseRedirect
from .models import Kid

# Create your views here.
def index(request):
	all_kids = Kid.objects.all()
	name = ""
	if request.method == "POST":
		name = request.POST.get("name", None)

		grade =request.POST.get("grade", None)
		if grade is None:
			grade = " "
		if(name == 'delete_all'):
			Kid.objects.all().delete()
		elif (len([x for x in all_kids if x.kid_name == name]) == 0):
			newkid = Kid()
			newkid.kid_name = name
			newkid.kid_grade = grade
			newkid.save()
			return HttpResponseRedirect('/')
		else:
			kid = Kid.objects.get(kid_name=name)
			setattr(kid, 'kid_signed_in', True)
			kid.save()
			return HttpResponseRedirect('/')

	return render(request, "Home/index.html", {'all_kids' : all_kids, 'kids_signed_in' : [x for x in all_kids if x.kid_signed_in == True]})
