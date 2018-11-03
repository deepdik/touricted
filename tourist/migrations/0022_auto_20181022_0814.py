# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0021_auto_20181022_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packageimages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(default='image Captions', max_length=120)),
            ],
        ),
        migrations.AlterModelOptions(
            name='hotelsforpackage',
            options={'verbose_name_plural': 'Hotels For Package'},
        ),
        migrations.RenameField(
            model_name='package',
            old_name='Image',
            new_name='BannerImage',
        ),
        migrations.AddField(
            model_name='packageimages',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Package_images', to='tourist.Package'),
        ),
    ]
