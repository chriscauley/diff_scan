# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
        ('main', '0006_screensize_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetest',
            name='design',
            field=models.ForeignKey(blank=True, to='media.Photo', null=True),
        ),
    ]
