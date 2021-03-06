# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-04 05:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, default=b'', max_length=250)),
                ('avatar', models.ImageField(blank=True, default=b'assets/avatar_default.svg', upload_to=b'avatars/')),
                ('gender', models.CharField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=500)),
                ('about', models.TextField(blank=True, max_length=1500)),
                ('groups', models.ManyToManyField(blank=True, to='staff.UserGroup')),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
