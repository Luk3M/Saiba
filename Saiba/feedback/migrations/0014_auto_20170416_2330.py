# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0013_auto_20170110_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='response_to',
        ),
        migrations.AddField(
            model_name='comment',
            name='response_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='feedback.Comment'),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
