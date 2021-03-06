# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0011_auto_20181019_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destination',
            options={'ordering': ('timestamp',), 'verbose_name_plural': 'Destinations'},
        ),
        migrations.AddField(
            model_name='destination',
            name='Best_time_for_travel',
            field=models.CharField(choices=[('january', 'JAN'), ('march', 'MAR'), ('april', 'APR')], default=0, max_length=120),
        ),
        migrations.AddField(
            model_name='package',
            name='cities',
            field=models.CharField(default=1, max_length=120),
        ),
    ]
