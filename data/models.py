from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Data(models.Model):

	name = models.CharField(max_length=30)
	about = models.TextField(default='-')
	fill = models.CharField(max_length=30, default='-')
	icon = models.CharField(max_length=50, default='-')
	
	def __str__(self):
		
		return self.name + ' | ' + str(self.pk)

