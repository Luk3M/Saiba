# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-09 00:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0017_auto_20170118_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 9, 0, 6, 51, 698000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 9, 0, 6, 51, 701000, tzinfo=utc)),
        ),
    ]
