# Generated by Django 4.1.2 on 2022-12-17 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_userprofile_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='id_user',
        ),
    ]
