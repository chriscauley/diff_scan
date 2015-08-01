# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_page_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetest',
            name='last_passed',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
