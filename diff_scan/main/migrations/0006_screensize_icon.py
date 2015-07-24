# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_pagetest_stable_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='screensize',
            name='icon',
            field=models.CharField(default='desktop', max_length=16, choices=[(b'desktop', b'Desktop'), (b'mobile', b'Mobile'), (b'tablet', b'Tablet')]),
            preserve_default=False,
        ),
    ]
