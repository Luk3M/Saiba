# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-16 01:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0014_auto_20161212_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='points',
            new_name='trending_points',
        ),
    ]
