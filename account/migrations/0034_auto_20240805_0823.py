# Generated by Django 3.0.11 on 2024-08-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0033_auto_20240717_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredpost',
            name='first_content',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='first_content',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
