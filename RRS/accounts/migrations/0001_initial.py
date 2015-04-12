# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('base', '0002_auto_20150325_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='accounts.ExtendedUser')),
                ('restaurant', models.ForeignKey(to='base.Restaurant')),
            ],
            options={
                'permissions': (('make_manual_reservation', 'Can make manual reservations'), ('edit_restaurant', "Can edit restaurant's details"), ('edit_menus', "Can edit restaurant's menus"), ('manage_staff', "Can manage restaurant's staff accounts"), ('customer_list', "Can view a list of restaurant's customers"), ('previous_reservations', "Can view a restaurant's reservation history")),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='accounts.ExtendedUser')),
            ],
            options={
                'permissions': (('make_reservation', 'Can make personal reservations'),),
            },
            bases=(models.Model,),
        ),
    ]
