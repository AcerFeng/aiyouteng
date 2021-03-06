# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-14 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SeriesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VerietyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=100)),
                ('play_num', models.CharField(max_length=50)),
                ('update_num', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
                ('score', models.CharField(max_length=10)),
                ('created_time', models.DateTimeField()),
                ('modified_time', models.DateTimeField()),
                ('movies_category', models.ManyToManyField(blank=True, to='aiyouteng.MoviesCategory')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aiyouteng.Platform')),
                ('veriety_category', models.ManyToManyField(blank=True, to='aiyouteng.VerietyCategory')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='video_category',
            field=models.ManyToManyField(blank=True, to='aiyouteng.VideoCategory'),
        ),
    ]
