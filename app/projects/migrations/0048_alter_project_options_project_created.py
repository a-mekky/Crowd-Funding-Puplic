# Generated by Django 4.0.1 on 2022-02-21 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0047_alter_comment_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-total_votes', '-total_upvotes']},
        ),
        migrations.AddField(
            model_name='project',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-20 19:54:29.589217+02'),
            preserve_default=False,
        ),
    ]