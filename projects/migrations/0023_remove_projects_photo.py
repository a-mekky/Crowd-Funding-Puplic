# Generated by Django 4.0.1 on 2022-02-19 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_alter_images_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='photo',
        ),
    ]
