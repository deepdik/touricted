# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0009_destination'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='type',
            new_name='Destination_type',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='PackageDay',
            new_name='PackageDays',
        ),
        migrations.AddField(
            model_name='destination',
            name='name',
            field=models.CharField(default=0, max_length=120),
        ),
    ]
