# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='carga_horaria',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='oferta',
            name='descripcion_del_trabajo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='oferta',
            name='posicion_cargo',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='oferta',
            name='profesion',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
