# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0052_auto_20181105_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerarydays',
            name='Inclusion',
            field=models.ManyToManyField(blank=True, null=True, to='tourist.Inclusion'),
        ),
    ]
