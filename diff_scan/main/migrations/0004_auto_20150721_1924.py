# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('main', '0003_auto_20150721_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screensize',
            old_name='site',
            new_name='sites',
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(default=1, to='sites.Site'),
            preserve_default=False,
        ),
    ]
