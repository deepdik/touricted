# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0004_auto_20181019_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='inclusion',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
