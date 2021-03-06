# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-04 05:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=2500)),
                ('description', models.CharField(blank=True, max_length=2500)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, default=b'', max_length=250, unique=True)),
                ('type', models.CharField(blank=True, max_length=100)),
                ('date_origin', models.CharField(blank=True, max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, upload_to=b'icon/')),
                ('icon_url', models.URLField(blank=True)),
                ('hidden', models.BooleanField(default=False)),
                ('images_locked', models.BooleanField(default=False)),
                ('videos_locked', models.BooleanField(default=False)),
                ('comments_locked', models.BooleanField(default=False)),
                ('trending_points', models.IntegerField(default=0)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='entry.Category')),
                ('editorship', models.ManyToManyField(blank=True, to='profile.Profile')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='EntryRedirect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=b'', max_length=250, unique=True)),
                ('entry', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='entry.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hidden', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='entry.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=2500)),
                ('code_name', models.CharField(blank=True, max_length=2500)),
                ('description', models.CharField(blank=True, max_length=2500)),
            ],
            options={
                'verbose_name_plural': 'status',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='entry.Status'),
        ),
    ]
