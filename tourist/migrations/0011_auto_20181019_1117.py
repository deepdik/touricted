# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0010_auto_20181019_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destination',
            options={'ordering': ('timestamp',), 'verbose_name_plural': 'Activities'},
        ),
        migrations.AddField(
            model_name='destination',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destination',
            name='Destination_type',
            field=models.CharField(choices=[('domestic', 'Domestic'), ('international', 'International')], max_length=120),
        ),
        migrations.AlterField(
            model_name='package',
            name='Destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tourist.Destination'),
        ),
    ]
