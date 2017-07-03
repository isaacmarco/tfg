# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0010_plan_sesiones_completadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='evaluar',
            field=models.BooleanField(default=False),
        ),
    ]
