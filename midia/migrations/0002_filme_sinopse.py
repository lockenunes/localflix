# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-24 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='sinopse',
            field=models.TextField(default='Sinopse texto...', verbose_name='Sinopse'),
        ),
    ]
