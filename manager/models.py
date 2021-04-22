from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Manager(models.Model):

	uuser = models.TextField()
	uemail = models.TextField(default='-')

	def __str__(self):
		
		return self.uuser + ' | ' + str(self.pk)
