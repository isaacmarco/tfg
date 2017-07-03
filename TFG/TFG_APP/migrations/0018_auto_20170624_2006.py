# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0017_plan_estado_riesgo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='estado_riesgo',
            new_name='rendimiento',
        ),
    ]
