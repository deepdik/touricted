# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0024_itinerarydays_inclusion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerarydays',
            name='Inclusion',
        ),
        migrations.AddField(
            model_name='itinerarydays',
            name='Inclusion',
            field=models.ManyToManyField(default=1, related_name='Inclusion', to='tourist.Inclusion'),
        ),
    ]
