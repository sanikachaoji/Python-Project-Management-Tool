# Generated by Django 2.2.1 on 2019-05-21 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj_tasks', '0009_task_task_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_project',
            new_name='project',
        ),
    ]