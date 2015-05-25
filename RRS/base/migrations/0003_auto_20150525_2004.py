# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150325_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='area',
        ),
        migrations.AddField(
            model_name='location',
            name='area',
            field=models.ForeignKey(default=1, to='base.Area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.FloatField(default=14.639344),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.FloatField(default=121.074266),
            preserve_default=False,
        ),
    ]
