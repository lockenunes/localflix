# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-13 15:48
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
                ('endereco_logradouro_tipo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Logradouro')),
                ('endereco_logradouro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Logradouro')),
                ('endereco_bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('endereco_numero', models.CharField(blank=True, default='S/N', max_length=5, null=True, verbose_name='Número')),
                ('endereco_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('endereco_referencia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referência')),
                ('endereco_cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('endereco_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('numero_de_oscar', models.IntegerField(default=0, verbose_name='Quantidade de Oscar')),
            ],
            options={
                'verbose_name_plural': 'Atores',
                'verbose_name': 'Ator',
            },
        ),
        migrations.CreateModel(
            name='BluRay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidades', models.PositiveIntegerField(default=0, verbose_name='Quantidade de unidades')),
                ('em_estoque', models.PositiveIntegerField(default=0, verbose_name='Em estoque')),
                ('duplo', models.BooleanField(default=False)),
                ('dual_layer', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'verbose_name': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('endereco_logradouro_tipo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Logradouro')),
                ('endereco_logradouro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Logradouro')),
                ('endereco_bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('endereco_numero', models.CharField(blank=True, default='S/N', max_length=5, null=True, verbose_name='Número')),
                ('endereco_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('endereco_referencia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referência')),
                ('endereco_cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('endereco_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('vip', models.BooleanField(default=0, verbose_name='VIP?')),
                ('pontos_fidelidade', models.PositiveIntegerField(default=0, verbose_name='Pontos de Fidelidade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dependente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('endereco_logradouro_tipo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Logradouro')),
                ('endereco_logradouro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Logradouro')),
                ('endereco_bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('endereco_numero', models.CharField(blank=True, default='S/N', max_length=5, null=True, verbose_name='Número')),
                ('endereco_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('endereco_referencia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referência')),
                ('endereco_cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('endereco_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.Cliente', verbose_name='Responsável')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Diretor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('endereco_logradouro_tipo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Logradouro')),
                ('endereco_logradouro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Logradouro')),
                ('endereco_bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('endereco_numero', models.CharField(blank=True, default='S/N', max_length=5, null=True, verbose_name='Número')),
                ('endereco_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('endereco_referencia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referência')),
                ('endereco_cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('endereco_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('especialidade', models.CharField(max_length=200, verbose_name='Especialidade')),
                ('numero_de_oscar', models.IntegerField(default=0, verbose_name='Quantidade de Oscar')),
            ],
            options={
                'verbose_name_plural': 'Diretores',
                'verbose_name': 'Diretor',
            },
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidades', models.PositiveIntegerField(default=0, verbose_name='Quantidade de unidades')),
                ('em_estoque', models.PositiveIntegerField(default=0, verbose_name='Em estoque')),
                ('duplo', models.BooleanField(default=False)),
                ('dual_layer', models.BooleanField(default=False)),
                ('regiao', models.PositiveIntegerField(default=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fantasia', models.CharField(max_length=200)),
                ('cnpj', models.CharField(blank=True, max_length=50, null=True, verbose_name='CNPJ')),
                ('endereco_logradouro_tipo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Logradouro')),
                ('endereco_logradouro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Logradouro')),
                ('endereco_bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('endereco_numero', models.CharField(blank=True, default='S/N', max_length=5, null=True, verbose_name='Número')),
                ('endereco_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('endereco_referencia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referência')),
                ('endereco_cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('endereco_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('ano_producao', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2016)], verbose_name='Ano de Produção')),
                ('numero_de_oscar', models.IntegerField(default=0, verbose_name='Quantidade de Oscar')),
                ('atores', models.ManyToManyField(to='locadora.Ator', verbose_name='Atores')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.Categoria', verbose_name='Categoria')),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.Diretor', verbose_name='Diretor')),
            ],
        ),
        migrations.AddField(
            model_name='dvd',
            name='fabricante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.Fabricante'),
        ),
        migrations.AddField(
            model_name='dvd',
            name='filme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.Filme'),
        ),
        migrations.AddField(
            model_name='bluray',
            name='fabricante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.Fabricante'),
        ),
        migrations.AddField(
            model_name='bluray',
            name='filme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.Filme'),
        ),
    ]
