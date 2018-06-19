from django.db import models

# Create your models here.
class Kid(models.Model):
	kid_name = models.CharField(max_length=40, default='None')
	kid_grade = models.IntegerField(default=7)
	kid_student_id = models.CharField(max_length=40, default='')

	time_entered = models.DateTimeField(auto_now=True)
	kid_signed_in = models.BooleanField(default=False)

	subject = models.CharField(max_length=40, default='None')
	place = models.CharField(max_length=40, default='None')
	reason = models.CharField(max_length=40, default='None')
	teacher_name = models.CharField(max_length=40, default='None')

	kid_field_names = ['kid_name', 'kid_grade', 'kid_student_id']

class Teacher(models.Model):
	teacher_name = models.CharField(max_length=40, default='None')	

class SignIn(models.Model):
	

	kid_name = models.CharField(max_length=40, default='None')
	kid_grade = models.IntegerField(default=7)
	kid_id =  models.IntegerField(default=7)

	teacher_name = models.CharField(max_length=40, default='None')

#	teacher = models.OneToOneField(
#		Teacher,
#        on_delete=models.CASCADE,
#    )

	time_entered = models.DateTimeField(auto_now=True)
	time_left = models.DateTimeField(auto_now=True)
	currently_signed_in = models.BooleanField(default=True)

	subject = models.CharField(max_length=40, default='None')
	place = models.CharField(max_length=40, default='None')
	reason = models.CharField(max_length=40, default='None')

#    teacher = models.OneToOneField(
#        settings.AUTH_USER_MODEL,
#        on_delete=models.CASCADE,
#    )

class BoxSignOut(models.Model):
	currently_signed_in =models.BooleanField(default=True)
	teacher_name = models.CharField(max_length=40, default='None')
	box_num = models.CharField(max_length=40, default='None')

