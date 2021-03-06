# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0032_auto_20181024_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='Best_time_for_travel_from',
            field=models.CharField(choices=[('january', 'JAN'), ('february', 'FEB'), ('march', 'MAR'), ('april', 'APR'), ('may', 'MAY'), ('june', 'JUN'), ('july', 'JUL'), ('august', 'AUG'), ('september', 'SEP')], max_length=120),
        ),
        migrations.AlterField(
            model_name='destination',
            name='Best_time_for_travel_to',
            field=models.CharField(choices=[('january', 'JAN'), ('february', 'FEB'), ('march', 'MAR'), ('april', 'APR'), ('may', 'MAY'), ('june', 'JUN'), ('july', 'JUL'), ('august', 'AUG'), ('september', 'SEP')], max_length=120),
        ),
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='facilities',
            field=models.TextField(),
        ),
    ]
