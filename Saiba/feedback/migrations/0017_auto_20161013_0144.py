# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0016_auto_20161013_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target_id',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]
