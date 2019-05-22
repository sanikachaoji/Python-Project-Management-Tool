from django import forms
from .models import Task, Project
class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['task_header']
		labels = {'text': ''}
		
class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project 
		fields = ['project']
		labels = {'text': ''}		
		