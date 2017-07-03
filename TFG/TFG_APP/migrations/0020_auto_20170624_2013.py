# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0019_plan_ponderacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='ponderacion',
            field=models.FloatField(default=0),
        ),
    ]
