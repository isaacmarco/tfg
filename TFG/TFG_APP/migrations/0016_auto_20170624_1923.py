# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0015_auto_20170624_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='fecha',
            field=models.DateTimeField(verbose_name='date created', default=django.utils.timezone.now),
        ),
    ]
