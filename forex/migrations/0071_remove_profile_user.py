# Generated by Django 3.2.16 on 2023-11-06 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0070_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
