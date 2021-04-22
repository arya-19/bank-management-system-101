from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Main(models.Model):

	name = models.CharField(max_length=50)
	about = models.TextField(default='-')
	phn = models.CharField(default='-', max_length=50)
	email = models.CharField(default='-', max_length=50)
	tw = models.CharField(default='-', max_length=50)
	fb = models.CharField(default='-', max_length=50)
	ig = models.CharField(default='-', max_length=50)
	ln = models.CharField(default='-', max_length=50)

	def __str__(self):
		
		return self.name + ' | ' + str(self.pk)
