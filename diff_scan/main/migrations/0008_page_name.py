# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_pagetest_design'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
