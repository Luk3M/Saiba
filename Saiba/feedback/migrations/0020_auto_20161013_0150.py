# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0019_auto_20161013_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='target_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
