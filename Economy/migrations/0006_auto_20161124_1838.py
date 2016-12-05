# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-24 18:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Economy', '0005_auto_20161121_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='datum')),
                ('startTime', models.TimeField(verbose_name='starttid')),
                ('endTime', models.TimeField(verbose_name='sluttid')),
            ],
            options={
                'verbose_name': 'arbetstimme',
                'verbose_name_plural': 'arbetstimmar',
            },
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='bikeSales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='cyklar'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='booksSales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='böcker'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='cafeSales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='café'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='card',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='kort'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='cash',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='kontanter'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='comment',
            field=models.CharField(max_length=150, null=True, verbose_name='kommentar'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='datum'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='foodShopSales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='gårdsbutik'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='iceCreamSales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='glass'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='other12Sales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='övrigt 12%'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='other25Sales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='övrigt 25%'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Economy.Employee', verbose_name='Signatur'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default=None, max_length=25, verbose_name='förnamn'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default=None, max_length=25, verbose_name='efternamn'),
        ),
        migrations.AddField(
            model_name='workinghours',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Economy.Employee'),
        ),
    ]
