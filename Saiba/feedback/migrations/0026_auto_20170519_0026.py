# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-19 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0025_auto_20170519_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='session',
            field=models.CharField(max_length=50),
        ),
    ]
