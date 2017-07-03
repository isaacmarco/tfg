# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0021_resultado_ponderacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='ponderacion',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=1),
        ),
    ]
