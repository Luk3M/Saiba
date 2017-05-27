# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-26 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0032_auto_20170513_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedirectEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=b'', max_length=250, unique=True)),
                ('entry', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='entry.Entry')),
            ],
        ),
    ]
