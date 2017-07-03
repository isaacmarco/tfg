# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0020_auto_20170624_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='ponderacion',
            field=models.FloatField(default=0),
        ),
    ]
