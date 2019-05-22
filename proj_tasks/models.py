from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	"""A task the user is adding"""
	project = models.CharField(max_length=200)
	date_added= models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		"""Return a string representation of the model."""
		return self.project
		
class Task(models.Model):
	ToDo = 'To_Do'
	InProgress ='In_Progress'
	Done='Done'
	task_status_choices = ((ToDo, 'To-Do'),(InProgress, 'In-Progress'),(Done, 'Done'),)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	task_header = models.CharField(max_length=200)
	task_Description = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)
	due_date = models.DateTimeField()
	task_status = models.CharField(max_length= 15, choices=task_status_choices, default=ToDo)
	attachments = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.task_header[:50] + "..." +":"+ self.task_Description[0:50]

class Entry(models.Model):
	"""Something specific learned about a topic"""
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	description = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = 'entries'
	def __str__(self):
		"""Return a string representation of the model."""
		return self.text[:50] + "..."		