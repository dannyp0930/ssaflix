# Generated by Django 3.2.6 on 2021-11-19 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='genres',
        ),
    ]