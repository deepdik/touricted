# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 09:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0063_auto_20181119_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='includedhotel',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='package',
            name='hotel',
        ),
        migrations.DeleteModel(
            name='IncludedHotel',
        ),
    ]
