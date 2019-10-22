# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0066_auto_20181119_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='activity',
            field=models.ManyToManyField(blank=True, to='tourist.Activity'),
        ),
        migrations.AddField(
            model_name='destination',
            name='category',
            field=models.ManyToManyField(blank=True, to='tourist.Category'),
        ),
        migrations.AddField(
            model_name='destination',
            name='inclusion',
            field=models.ManyToManyField(blank=True, to='tourist.Inclusion'),
        ),
        migrations.AddField(
            model_name='destination',
            name='max_package_price',
            field=models.PositiveIntegerField(default=50000),
        ),
        migrations.AddField(
            model_name='destination',
            name='max_pkg_days',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='destination',
            name='min_package_price',
            field=models.PositiveIntegerField(default=4000),
        ),
        migrations.AddField(
            model_name='destination',
            name='min_pkg_days',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='destination',
            name='number_of_packages',
            field=models.PositiveIntegerField(default=50),
        ),
    ]