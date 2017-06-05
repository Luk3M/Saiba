# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-04 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=250, unique=True)),
                ('label', models.CharField(max_length=250)),
                ('assign_to_staff', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=250, unique=True)),
                ('label', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='usergroup',
            name='permissions',
            field=models.ManyToManyField(to='staff.UserPermission'),
        ),
    ]