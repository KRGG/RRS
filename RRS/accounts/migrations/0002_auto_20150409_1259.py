# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150325_1702'),
        ('auth', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
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
        migrations.RenameModel(
            old_name='Customer',
            new_name='CustomerProfile',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.CreateModel(
            name='UserProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='user',
            field=models.OneToOneField(to='accounts.UserProxy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='user',
            field=models.OneToOneField(to='accounts.UserProxy'),
            preserve_default=True,
        ),
    ]
