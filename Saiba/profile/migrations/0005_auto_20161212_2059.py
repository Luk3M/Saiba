# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-12 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20161004_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[(b'Ele', b'Ele'), (b'Ela', b'Ela'), (b'Ele(a)', b'Ele(a)')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
