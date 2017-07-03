# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0012_remove_plan_completado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='dificultad',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='tipo_operaciones',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='resultados',
        ),
        migrations.AddField(
            model_name='plan',
            name='magnitud_item',
            field=models.CharField(max_length=100, default='normal'),
        ),
        migrations.AddField(
            model_name='plan',
            name='tiempo_entre_items',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='plan',
            name='tiempo_limite_item',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='resultado',
            name='porcentaje_contestado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='numero_sesiones',
            field=models.IntegerField(default=3),
        ),
    ]
