# Generated by Django 4.1.2 on 2022-12-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[(1, 'Draft'), (2, 'Publish')], default=1, max_length=10),
        ),
    ]
