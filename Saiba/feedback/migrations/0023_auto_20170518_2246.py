# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-19 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0022_view_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='session',
            field=models.CharField(max_length=50),
        ),
    ]