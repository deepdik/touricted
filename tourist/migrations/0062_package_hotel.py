# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0061_remove_category_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='hotel',
            field=models.ManyToManyField(to='tourist.Hotel'),
        ),
    ]
