# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150412_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to='accounts.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to='accounts.UserProfile'),
            preserve_default=True,
        ),
    ]
