# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerprofile',
            options={'permissions': (('make_reservation', 'Can make personal reservations'),)},
        ),
        migrations.AlterModelOptions(
            name='staffprofile',
            options={'permissions': (('make_manual_reservation', 'Can make manual reservations'), ('edit_restaurant', "Can edit restaurant's details"), ('edit_menus', "Can edit restaurant's menus"), ('manage_staff', "Can manage restaurant's staff accounts"), ('customer_list', "Can view a list of restaurant's customers"), ('previous_reservations', "Can view a restaurant's reservation history"))},
        ),
    ]
