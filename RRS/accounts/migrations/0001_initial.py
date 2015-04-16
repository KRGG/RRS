# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('base', '0002_auto_20150325_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('type', models.IntegerField(default=1, choices=[(1, b'Customer'), (2, b'Staff')])),
                ('restaurant', models.ForeignKey(blank=True, to='base.Restaurant', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
