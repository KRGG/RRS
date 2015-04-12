# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150325_1702'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('restaurant', models.ForeignKey(to='base.Restaurant')),
            ],
            options={
                'permissions': (('edit_restaurant', "Can edit a restaurant's details"),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='user',
            field=models.OneToOneField(to='accounts.ExtendedUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='user',
            field=models.OneToOneField(to='accounts.ExtendedUser'),
            preserve_default=True,
        ),
    ]
