from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['courseName']) < 5:
			errors['courseName'] = "Course Name should be more than 5 Characters"
		if len(postData['courseDescription']) < 15:
			errors['courseDescription'] = "Description should be more than 15 Characters"
		return errors

class Course(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# connect an instance of BlogManager to our blog Model
	objects = UserManager()
