# Generated by Django 5.0.6 on 2024-05-08 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voltasapp', '0002_alter_washingmachine_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='washingmachine',
            name='price',
        ),
        migrations.RemoveField(
            model_name='washingmachine',
            name='title',
        ),
    ]
