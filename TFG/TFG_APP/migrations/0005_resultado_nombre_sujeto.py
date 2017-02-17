# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0004_auto_20170215_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='nombre_sujeto',
            field=models.CharField(max_length=100, default='nombre sujeto'),
        ),
    ]
