# Generated by Django 3.1.5 on 2021-02-01 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
