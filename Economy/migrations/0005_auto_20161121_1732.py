# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-21 17:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Economy', '0004_auto_20161121_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='personNo',
        ),
        migrations.AddField(
            model_name='employee',
            name='ArbAvg',
            field=models.DecimalField(decimal_places=2, default=0.25, max_digits=3),
        ),
        migrations.AddField(
            model_name='employee',
            name='drawTax',
            field=models.BooleanField(default=True, help_text='skall preliminärskatt dras från lönen?', verbose_name='Dra preliminärskatt'),
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=25, null=True, verbose_name='förnamn'),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=25, null=True, verbose_name='efternamn'),
        ),
        migrations.AddField(
            model_name='employee',
            name='person_number',
            field=models.IntegerField(null=True, verbose_name='Personnummer'),
        ),
        migrations.AddField(
            model_name='employee',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=33.0, help_text='Preliminärskatt att dra från lönen', max_digits=4, verbose_name='preliminärskatt'),
        ),
        migrations.AlterField(
            model_name='dagskassa',
            name='signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Economy.Employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hours_worked',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='arbetade timmar'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='anställd'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='wage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, verbose_name='Lön'),
        ),
    ]