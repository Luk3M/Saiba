# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-27 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20170527_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bpost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.BPostCategory'),
        ),
    ]
