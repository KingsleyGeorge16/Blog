# Generated by Django 4.1.2 on 2023-01-31 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_featuredpost_section1_featuredpost_section2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featuredpost',
            old_name='section1',
            new_name='add_more',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='section1',
            new_name='add_more',
        ),
        migrations.RemoveField(
            model_name='featuredpost',
            name='section2',
        ),
        migrations.RemoveField(
            model_name='featuredpost',
            name='section3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='section2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='section3',
        ),
    ]
