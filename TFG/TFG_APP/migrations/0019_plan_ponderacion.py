# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0018_auto_20170624_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='ponderacion',
            field=models.IntegerField(default=0),
        ),
    ]
