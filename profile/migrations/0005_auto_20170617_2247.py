# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-18 01:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20170617_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 24, 22, 47, 48, 550012)),
        ),
    ]
