# Generated by Django 5.0.6 on 2024-05-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voltasapp', '0013_imageupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageUpload',
        ),
    ]