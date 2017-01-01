# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-27 12:33
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0010_auto_20161227_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dagskassa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='datum')),
                ('cash', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='kontanter')),
                ('card', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='kort')),
                ('cafeSales', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='café')),
                ('iceCreamSales', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='glass')),
                ('foodShopSales', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='gårdsbutik')),
                ('bikeSales', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='cyklar')),
                ('booksSales', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='böcker')),
                ('other12Sales', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='övrigt 12%')),
                ('other25Sales', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='övrigt 25%')),
                ('comment', models.CharField(max_length=150, null=True, verbose_name='kommentar')),
            ],
            options={
                'ordering': ('date',),
                'verbose_name_plural': 'dagskassor',
                'verbose_name': 'dagskassa',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('person_number', models.IntegerField(null=True, verbose_name='Personnummer')),
                ('wage', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Lön')),
                ('hours_worked', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='arbetade timmar')),
                ('tax', models.DecimalField(decimal_places=2, default=33.0, help_text='Preliminärskatt att dra från lönen', max_digits=4, verbose_name='preliminärskatt')),
                ('drawTax', models.BooleanField(default=True, help_text='skall preliminärskatt dras från lönen?', verbose_name='Dra preliminärskatt')),
                ('ArbAvg', models.DecimalField(decimal_places=2, default=0.25, max_digits=3)),
            ],
            options={
                'verbose_name_plural': 'anställda',
                'verbose_name': 'anställd',
            },
            bases=('auth.staff', models.Model),
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='datum')),
                ('startTime', models.TimeField(verbose_name='starttid')),
                ('endTime', models.TimeField(verbose_name='sluttid')),
                ('added', models.DateTimeField(default=datetime.datetime.now, verbose_name='Tillagd')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Economy.Employee', verbose_name='anställd')),
            ],
            options={
                'verbose_name_plural': 'arbetstimmar',
                'verbose_name': 'arbetstimme',
            },
        ),
        migrations.AddField(
            model_name='dagskassa',
            name='signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Economy.Employee', verbose_name='Signatur'),
        ),
        migrations.AlterUniqueTogether(
            name='workinghours',
            unique_together=set([('employee', 'date', 'added')]),
        ),
        migrations.AlterUniqueTogether(
            name='dagskassa',
            unique_together=set([('date', 'cash', 'card', 'signature')]),
        ),
    ]
