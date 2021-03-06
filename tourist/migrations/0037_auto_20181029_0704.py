# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0036_auto_20181025_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hoteltest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilities', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='facilities',
        ),
        migrations.AddField(
            model_name='hoteltest',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hotel_test', to='tourist.Hotel'),
        ),
    ]
