# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-20 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0026_auto_20170519_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='session',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
