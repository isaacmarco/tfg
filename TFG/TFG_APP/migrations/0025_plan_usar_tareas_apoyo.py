# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0024_auto_20170629_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='usar_tareas_apoyo',
            field=models.BooleanField(default=False),
        ),
    ]
