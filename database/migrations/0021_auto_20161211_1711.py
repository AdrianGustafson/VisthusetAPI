# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-11 17:11
from __future__ import unicode_literals

import database.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_auto_20161211_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='longest_prel',
            field=models.DateTimeField(blank=True, null=True, validators=[database.validators.validate_preliminary], verbose_name='längsta preliminärbokning'),
        ),
    ]