# Generated by Django 3.0.11 on 2024-08-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0034_auto_20240805_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredpost',
            name='first_content',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='first_content',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
