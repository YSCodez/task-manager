# Generated by Django 4.1 on 2024-07-31 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tskhandler', '0004_taskalloca_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskalloca',
            old_name='date',
            new_name='updated_at',
        ),
    ]
