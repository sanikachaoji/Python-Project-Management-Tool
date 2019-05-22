from django import forms
from .models import Task, Project
class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['task_header', 'task_Description','due_date','task_status', 'project','owner','attachments']
		labels = {'text':	''}
		
class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project 
		fields = ['project']
		labels = {'text': ''}		
		