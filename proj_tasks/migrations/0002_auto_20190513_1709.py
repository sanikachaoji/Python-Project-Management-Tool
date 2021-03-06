# Generated by Django 2.2.1 on 2019-05-14 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj_tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task_category',
            options={'verbose_name_plural': 'Task_Categories'},
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_header', models.TextField()),
                ('task_Description', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_tasks.Task_Category')),
            ],
        ),
    ]
