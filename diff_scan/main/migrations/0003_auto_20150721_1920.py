# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('main', '0002_page_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='page',
            name='diff_image',
        ),
        migrations.RemoveField(
            model_name='page',
            name='screen_sizes',
        ),
        migrations.RemoveField(
            model_name='page',
            name='site',
        ),
        migrations.RemoveField(
            model_name='page',
            name='stable_image',
        ),
        migrations.RemoveField(
            model_name='page',
            name='test_image',
        ),
        migrations.AddField(
            model_name='pagetest',
            name='accepted',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pagetest',
            name='diff_image',
            field=models.ImageField(null=True, upload_to=b'diffs', blank=True),
        ),
        migrations.AddField(
            model_name='pagetest',
            name='error_code',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pagetest',
            name='page',
            field=models.ForeignKey(default=1, to='main.Page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagetest',
            name='screensize',
            field=models.ForeignKey(default=1, to='main.ScreenSize'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagetest',
            name='test_image',
            field=models.ImageField(null=True, upload_to=b'screenshots', blank=True),
        ),
        migrations.AddField(
            model_name='screensize',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
        ),
    ]
