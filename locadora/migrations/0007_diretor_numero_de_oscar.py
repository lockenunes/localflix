# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-12 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0006_auto_20160812_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='diretor',
            name='numero_de_oscar',
            field=models.IntegerField(default=0, verbose_name='Quantidade de Oscar'),
        ),
    ]
