# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0011_plan_evaluar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='completado',
        ),
    ]
