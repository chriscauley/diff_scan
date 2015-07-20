# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.TextField()),
                ('stable_image', models.ImageField(null=True, upload_to=b'screenshots', blank=True)),
                ('test_image', models.ImageField(null=True, upload_to=b'screenshots', blank=True)),
                ('diff_image', models.ImageField(null=True, upload_to=b'diffs', blank=True)),
                ('accepted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScreenSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.IntegerField(default=0, help_text=b'In pixels; 0 will default to an automatic size')),
                ('height', models.IntegerField(default=0, help_text=b'In pixels; 0 will default to an automatic size')),
                ('name', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='screen_sizes',
            field=models.ManyToManyField(to='main.ScreenSize', blank=True),
        ),
    ]
