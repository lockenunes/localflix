# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-12 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0003_auto_20160812_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='ano_producao',
            field=models.PositiveIntegerField(verbose_name='Data de Produção'),
        ),
    ]
