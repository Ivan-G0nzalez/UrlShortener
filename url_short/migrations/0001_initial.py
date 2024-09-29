# Generated by Django 5.1.1 on 2024-09-29 20:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, unique=True)),
                ('shortcode', models.CharField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(6)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
    ]
