# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='last_accessed',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]