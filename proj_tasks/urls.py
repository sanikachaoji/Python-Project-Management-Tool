

from django.urls import path

from . import views

app_name = 'proj_tasks'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
	# Show all tasks.
    path('projects/', views.projects, name='projects'),
	# Detail page for a single task.
    path('projects/<int:project_id>/', views.project, name='project'),
	# Page for adding a new task.
    path('new_project/', views.new_project, name='new_project'),
	path('new_task/<int:project_id>', views.new_task, name='new_task'),
	path('edit_task/<int:task_id>', views.edit_task, name='edit_task'),
	
]