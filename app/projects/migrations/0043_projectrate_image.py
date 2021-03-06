# Generated by Django 4.0.1 on 2022-02-20 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
        ('projects', '0042_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_upvote', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='projects/slider/')),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
