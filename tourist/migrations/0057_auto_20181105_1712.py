# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0056_itinerarydays_inclusion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerarydays',
            name='Inclusion',
            field=models.ManyToManyField(to='tourist.Inclusion'),
        ),
    ]