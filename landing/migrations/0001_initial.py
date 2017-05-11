# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('V', 'VENDER'), ('C', 'COMPRAR')], max_length=1)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('valor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='anuncio',
            name='registro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Registro'),
        ),
    ]
