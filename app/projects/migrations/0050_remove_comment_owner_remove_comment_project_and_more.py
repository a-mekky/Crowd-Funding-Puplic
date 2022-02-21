# Generated by Django 4.0.1 on 2022-02-21 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0049_project_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='project',
        ),
        migrations.RemoveField(
            model_name='image',
            name='project',
        ),
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
        migrations.AlterUniqueTogether(
            name='report',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='report',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='report',
            name='project',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
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
            name='Report',
        ),
    ]