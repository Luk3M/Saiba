# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-13 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0031_entry_icon_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'status'},
        ),
        migrations.AddField(
            model_name='status',
            name='code_name',
            field=models.CharField(blank=True, max_length=2500),
        ),
    ]
