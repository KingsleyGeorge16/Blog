# Generated by Django 3.0.11 on 2024-07-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0032_auto_20240712_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='first_content',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
