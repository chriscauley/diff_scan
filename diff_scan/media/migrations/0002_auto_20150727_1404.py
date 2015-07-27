# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miscfile',
            name='md5',
            field=models.CharField(default='none', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='md5',
            field=models.CharField(default='none', max_length=32),
            preserve_default=False,
        ),
    ]
