# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0055_remove_itinerarydays_inclusion'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerarydays',
            name='Inclusion',
            field=models.ManyToManyField(blank=True, to='tourist.Inclusion'),
        ),
    ]