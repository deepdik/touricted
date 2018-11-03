# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0003_auto_20181019_0733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='activity',
        ),
        migrations.AddField(
            model_name='package',
            name='activity',
            field=models.ManyToManyField(default=2, to='tourist.Activity'),
        ),
        migrations.RemoveField(
            model_name='package',
            name='inclusion',
        ),
        migrations.AddField(
            model_name='package',
            name='inclusion',
            field=models.ManyToManyField(default=1, to='tourist.Inclusion'),
        ),
    ]
