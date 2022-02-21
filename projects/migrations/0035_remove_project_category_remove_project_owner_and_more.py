# Generated by Django 4.0.2 on 2022-02-20 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_projectrate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='projectrate',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectrate',
            name='user',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectRate',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
