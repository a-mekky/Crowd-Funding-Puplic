# Generated by Django 4.0.2 on 2022-02-20 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0039_alter_comment_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
