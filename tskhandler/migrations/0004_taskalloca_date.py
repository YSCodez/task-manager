# Generated by Django 4.1 on 2024-07-31 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tskhandler', '0003_remove_taskalloca_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskalloca',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
