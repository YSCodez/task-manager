# Generated by Django 4.1 on 2024-07-31 08:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tskhandler', '0005_rename_date_taskalloca_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskalloca',
            name='timestamp',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]