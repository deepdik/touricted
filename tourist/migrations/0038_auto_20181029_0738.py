# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0037_auto_20181029_0704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hoteltest',
            old_name='facilities',
            new_name='facilitiy',
        ),
        migrations.AddField(
            model_name='hotel',
            name='facilities',
            field=models.TextField(null=True),
        ),
    ]
