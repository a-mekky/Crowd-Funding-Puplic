# Generated by Django 4.0.1 on 2022-02-17 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_rename_category_id_projects_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.category'),
            preserve_default=False,
        ),
    ]