# Generated by Django 3.0.11 on 2024-05-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_auto_20240508_0741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewpost',
            name='author',
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='writer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
