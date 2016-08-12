# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-12 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0008_auto_20160812_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme',
            name='categorias',
        ),
        migrations.AddField(
            model_name='filme',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='locadora.Categoria', verbose_name='Categoria'),
            preserve_default=False,
        ),
    ]
