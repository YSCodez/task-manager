# Generated by Django 4.1 on 2024-07-31 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tskhandler', '0006_taskalloca_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskalloca',
            name='timestamp',
        ),
    ]
