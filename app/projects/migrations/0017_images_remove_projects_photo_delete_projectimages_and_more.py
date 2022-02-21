# Generated by Django 4.0.1 on 2022-02-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_alter_projectimages_image_alter_projects_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='projects',
            name='photo',
        ),
        migrations.DeleteModel(
            name='ProjectImages',
        ),
        migrations.AddField(
            model_name='projects',
            name='photo',
            field=models.ManyToManyField(to='projects.Images'),
        ),
    ]
