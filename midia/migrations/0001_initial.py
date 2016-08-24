# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-24 14:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('end_tipo_logradouro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Logradouro')),
                ('end_logradouro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Logradouro')),
                ('end_bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('end_numero', models.CharField(blank=True, default='S/N', max_length=5, null=True, verbose_name='Número')),
                ('end_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('end_referencia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referência')),
                ('end_cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('end_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('numero_de_oscar', models.IntegerField(default=0, verbose_name='Quantidade de Oscar')),
            ],
            options={
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Diretor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('end_tipo_logradouro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Logradouro')),
                ('end_logradouro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Logradouro')),
                ('end_bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('end_numero', models.CharField(blank=True, default='S/N', max_length=5, null=True, verbose_name='Número')),
                ('end_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('end_referencia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referência')),
                ('end_cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('end_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('especialidade', models.CharField(max_length=200, verbose_name='Especialidade')),
                ('numero_de_oscar', models.IntegerField(default=0, verbose_name='Quantidade de Oscar')),
            ],
            options={
                'verbose_name': 'Diretor',
                'verbose_name_plural': 'Diretores',
            },
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('ano_producao', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2016)], verbose_name='Ano de Produção')),
                ('numero_de_oscar', models.IntegerField(default=0, verbose_name='Quantidade de Oscar')),
                ('atores', models.ManyToManyField(to='midia.Ator', verbose_name='Atores')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='midia.Categoria', verbose_name='Categoria')),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='midia.Diretor', verbose_name='Diretor')),
            ],
        ),
    ]
