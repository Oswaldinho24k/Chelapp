# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-29 22:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
