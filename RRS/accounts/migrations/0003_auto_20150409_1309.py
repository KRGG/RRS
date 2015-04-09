# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('accounts', '0002_auto_20150409_1259'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProxy',
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='user',
            field=models.OneToOneField(to='accounts.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='user',
            field=models.OneToOneField(to='accounts.UserProfile'),
            preserve_default=True,
        ),
    ]
