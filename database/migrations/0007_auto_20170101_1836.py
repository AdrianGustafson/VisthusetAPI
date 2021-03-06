# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-01 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_lunchbooking_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lunch',
            name='bookings',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='bookings',
        ),
        migrations.RemoveField(
            model_name='utilities',
            name='bookings',
        ),
        migrations.AddField(
            model_name='roomsbooking',
            name='room',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='database.Rooms'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lunchbooking',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='database.Lunch'),
        ),
    ]
