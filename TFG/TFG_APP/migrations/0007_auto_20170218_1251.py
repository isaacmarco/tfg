# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0006_resultado_sujeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resultado',
            name='porcentaje_acierto',
            field=models.IntegerField(default=0),
        ),
    ]
