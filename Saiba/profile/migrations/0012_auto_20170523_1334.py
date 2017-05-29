# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-23 16:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0011_auto_20170522_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='groups',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='staff.UserGroup'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]