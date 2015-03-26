# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='menu',
            field=models.ManyToManyField(to='base.Menu', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='website',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
