# Generated by Django 4.0.1 on 2022-02-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_project_alter_images_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='projects.Tags'),
        ),
    ]
