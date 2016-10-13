# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 01:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20161002_0226'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0003_auto_20160922_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=250)),
                ('is_positive', models.BooleanField(default=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feedback.Comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=250)),
                ('is_positive', models.BooleanField(default=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('media', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gallery.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=250)),
                ('is_positive', models.BooleanField(default=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('media', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gallery.Video')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]