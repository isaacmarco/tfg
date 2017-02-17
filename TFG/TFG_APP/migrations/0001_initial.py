# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluadoresSujetos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_sujeto', models.IntegerField(default=0)),
                ('id_evaluador', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Evaluador-Sujeto',
                'verbose_name_plural': 'Evaluadores-Sujetos',
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_sujeto', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField(verbose_name='date created', default=datetime.datetime.now)),
                ('evaluacion', models.BooleanField(default=False)),
                ('resultados', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Resultado',
                'verbose_name_plural': 'Resultados',
            },
        ),
    ]
