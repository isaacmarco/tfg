# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0022_auto_20170626_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='ponderacion',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=1),
        ),
    ]
