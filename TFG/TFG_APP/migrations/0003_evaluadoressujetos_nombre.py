# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0002_evaluadoressujetos_usuario_propietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluadoressujetos',
            name='nombre',
            field=models.CharField(max_length=100, default='nombre'),
        ),
    ]
