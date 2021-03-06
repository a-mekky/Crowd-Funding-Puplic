# Generated by Django 4.0.1 on 2022-02-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projects_total_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='projects',
            name='general_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
