# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-10 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0010_auto_20170110_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_NSFW',
        ),
        migrations.AddField(
            model_name='reply',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]