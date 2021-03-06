# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-04 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(blank=True, to='home.Tag'),
        ),
        migrations.AddField(
            model_name='bpost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.BPostCategory'),
        ),
    ]
