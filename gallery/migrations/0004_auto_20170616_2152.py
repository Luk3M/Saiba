# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-17 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20170606_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(blank=True, upload_to='icon/'),
        ),
        migrations.AlterField(
            model_name='state',
            name='code_name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
