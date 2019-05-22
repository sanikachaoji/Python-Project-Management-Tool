from django.shortcuts import render, get_object_or_404
from .models import Task
from .models import Project
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, ProjectForm

def index(request):
	"""The home page for Project management"""
	return render(request, 'proj_tasks/index.html')

@login_required
def projects(request):
    """Show all topics."""
    projects = Project.objects.filter(owner=request.user).order_by('date_added')
    context = {'projects': projects}
    return render(request, 'proj_tasks/projects.html', context)

@login_required
def project(request, project_id):
    """Show a single topic, and all its entries."""
    project = get_object_or_404(Project, id=project_id)
    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404
        
    tasks = project.task_set.order_by('-date_added')
    context = {'project': project, 'tasks': tasks}
    return render(request, 'proj_tasks/project.html', context)

@login_required
def new_project(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProjectForm()
    else:
        # POST data submitted; process data.
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner = request.user
            new_project.save()
            return HttpResponseRedirect(reverse('proj_tasks:projects'))

    context = {'form': form}
    return render(request, 'proj_tasks/new_project.html', context)

@login_required
def new_task(request, project_id):
    """Add a new entry for a particular topic."""
    project = Project.objects.get(id=project_id)
    if project.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TaskForm()        
    else:
        # POST data submitted; process data.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.project = project
            new_task.save()
            return HttpResponseRedirect(reverse('proj_tasks:project',
                                        args=[project_id]))
    
    context = {'project': project, 'form': form}
    return render(request, 'proj_tasks/new_task.html', context)

@login_required
def edit_task(request, task_id):
    """Edit an existing task."""
    task = Task.objects.get(id=task_id)
    project = task.project
    if project.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = TaskForm(instance=task)
    else:
        # POST data submitted; process data.
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('proj_tasks:project',
                                        args=[project.id]))
    
    context = {'task': task, 'project': project, 'form': form}
    return render(request, 'proj_tasks/edit_task.html', context)	
'''	
@login_required
def tasks(request):
	"""Show all topics."""
	tasks = Project.objects.order_by('date_added')
	context = {'tasks': tasks}
	return render(request, 'proj_tasks/tasks.html', context)
@login_required	
def task(request, task_id):
	"""Show a single task and all its entries."""
	task = Task.objects.get(category_id=task_id)
	context = {'task': task}
	
	return render(request, 'proj_tasks/task.html', context)	
@login_required	
def new_task(request):
	"""Add a new topic."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TaskForm()
	else:
		# POST data submitted; process data.
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('proj_tasks:tasks'))
	context = {'form': form}
	return render(request, 'proj_tasks/new_task.html', context)
	
def new_proj(request):
	
'''	