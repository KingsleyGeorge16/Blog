# Generated by Django 4.1.2 on 2023-01-29 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0014_post_header_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
