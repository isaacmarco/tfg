# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0009_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='sesiones_completadas',
            field=models.IntegerField(default=0),
        ),
    ]
