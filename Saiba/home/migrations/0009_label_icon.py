# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20161013_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='icon',
            field=models.ImageField(blank=True, default=b'labels/base.png', upload_to=b'labels/'),
        ),
    ]