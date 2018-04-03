from django.db import models

# Create your models here.
class Kid(models.Model):
	kid_name = models.CharField(max_length=40, default='None')
	kid_grade = models.IntegerField(max_length=20, default=7)
	kid_signed_in = models.BooleanField(default=False)

