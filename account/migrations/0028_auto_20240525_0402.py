# Generated by Django 3.0.11 on 2024-05-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_auto_20240508_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=300),
        ),
    ]
