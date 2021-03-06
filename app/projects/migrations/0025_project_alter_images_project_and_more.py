# Generated by Django 4.0.1 on 2022-02-19 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
        ('projects', '0024_remove_projects_user_projects_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('total_target', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('general_rate', models.IntegerField(default=0)),
                ('is_deleted', models.BooleanField(default=False)),
                ('main_photo', models.ImageField(upload_to='projects/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.category')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
        migrations.AlterField(
            model_name='images',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
        migrations.AlterField(
            model_name='projectimages',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
