# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0016_auto_20170624_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='estado_riesgo',
            field=models.CharField(max_length=50, default='normal'),
        ),
    ]
