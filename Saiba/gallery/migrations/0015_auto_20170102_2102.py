# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_auto_20170102_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_origin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='date_origin',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
