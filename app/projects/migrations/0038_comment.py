# Generated by Django 4.0.2 on 2022-02-20 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0037_projectrate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projects.project')),
            ],
        ),
    ]
