# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20161013_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='icon',
            field=models.ImageField(default=b'/label/base.png', upload_to=b''),
        ),
    ]