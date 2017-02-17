# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0003_evaluadoressujetos_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluadoressujetos',
            name='nombre',
        ),
        migrations.AddField(
            model_name='evaluadoressujetos',
            name='nombre_evaluador',
            field=models.CharField(max_length=100, default='nombre evaluador'),
        ),
        migrations.AddField(
            model_name='evaluadoressujetos',
            name='nombre_sujeto',
            field=models.CharField(max_length=100, default='nombre sujeto'),
        ),
    ]
