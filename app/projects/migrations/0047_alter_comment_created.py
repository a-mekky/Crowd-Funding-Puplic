# Generated by Django 4.0.1 on 2022-02-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0046_alter_comment_options_comment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
