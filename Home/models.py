from django.db import models

# Create your models here.
class Kid(models.Model):
	kid_name = models.CharField(max_length=40, default='None')
	kid_grade = models.IntegerField(default=7)
	kid_signed_in = models.BooleanField(default=False)

class Teacher(models.Model):
	techer_name = models.CharField(max_length=40, default='None')

class SignIn(models.Model):
	kid = models.OneToOneField(
       Kid,
        on_delete=models.CASCADE,
	)
#	teacher = models.OneToOneField(
#		Teacher,
#        on_delete=models.CASCADE,
#    )

	time_entered = models.DateTimeField(auto_now=True)
	time_left = models.DateTimeField(auto_now=True)

	subject = models.CharField(max_length=40, default='None')
	place = models.CharField(max_length=40, default='None')
	reason = models.CharField(max_length=40, default='None')

#    teacher = models.OneToOneField(
#        settings.AUTH_USER_MODEL,
#        on_delete=models.CASCADE,
#    )

