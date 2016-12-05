# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-04 20:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Economy', '0007_auto_20161124_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='workinghours',
            name='added',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Tillagd'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='wage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Lön'),
        ),
    ]
