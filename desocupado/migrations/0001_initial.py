# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('inicioContrato', models.DateField()),
                ('finContrato', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cuit', models.CharField(max_length=30)),
                ('razonSocial', models.CharField(max_length=50)),
                ('activa', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('activa', models.BooleanField()),
                ('inicioContrato', models.DateField()),
                ('finContrato', models.DateField()),
                ('empresa', models.ForeignKey(to='desocupado.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fechaDeNacimiento', models.DateField()),
                ('dni', models.CharField(max_length=20)),
                ('desocupado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipoDeTrabajo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='tipoDeTrabajoQuePuedeRealizar',
            field=models.ForeignKey(to='desocupado.Rubro'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='necesidad',
            field=models.ForeignKey(to='desocupado.Rubro'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='rubro',
            field=models.ForeignKey(to='desocupado.Rubro'),
        ),
        migrations.AddField(
            model_name='empleo',
            name='empresa',
            field=models.ForeignKey(to='desocupado.Empresa'),
        ),
        migrations.AddField(
            model_name='empleo',
            name='oferta',
            field=models.ForeignKey(to='desocupado.Oferta'),
        ),
        migrations.AddField(
            model_name='empleo',
            name='persona',
            field=models.ForeignKey(to='desocupado.Persona'),
        ),
    ]
