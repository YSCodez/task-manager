# Generated by Django 4.1 on 2024-07-31 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tskhandler', '0002_remove_taskalloca_time_alter_taskalloca_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskalloca',
            name='date',
        ),
    ]
