# Generated by Django 4.0.1 on 2022-02-17 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_rename_category_projects_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='category_id',
            new_name='category',
        ),
    ]
