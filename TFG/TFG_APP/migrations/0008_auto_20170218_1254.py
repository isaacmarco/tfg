# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0007_auto_20170218_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultado',
            old_name='evaluacion',
            new_name='es_evaluacion',
        ),
        migrations.RenameField(
            model_name='resultado',
            old_name='duracion',
            new_name='tiempo_empleado',
        ),
    ]
