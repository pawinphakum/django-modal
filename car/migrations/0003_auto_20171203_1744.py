# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_last_accessed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='last_accessed',
            field=models.DateTimeField(null=True),
        ),
    ]
