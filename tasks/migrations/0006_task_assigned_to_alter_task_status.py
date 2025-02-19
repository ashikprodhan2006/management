# Generated by Django 5.1.5 on 2025-02-17 13:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_delete_event_remove_task_assigned_to_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('PENDING', 'Pending')], default='PENDING', max_length=15),
        ),
    ]
