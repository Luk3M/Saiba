# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-17 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20170604_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='action_type',
            field=models.CharField(choices=[('0', 'Unknown'), ('1', 'New comment'), ('2', 'New reply'), ('3', 'New entry'), ('4', 'New image'), ('5', 'New video'), ('6', 'Edit entry'), ('7', 'Edit image'), ('8', 'Edit video')], default='0', max_length=1),
        ),
    ]
