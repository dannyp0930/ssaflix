# Generated by Django 3.2.7 on 2021-11-19 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='genres',
        ),
    ]
