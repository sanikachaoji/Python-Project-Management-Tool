from django.contrib import admin

from proj_tasks.models import Project, Task
admin.site.register(Project)
admin.site.register(Task)
#admin.site.register(Entry)