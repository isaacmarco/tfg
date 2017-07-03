# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('TFG_APP', '0013_auto_20170619_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='fecha',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2017, 6, 24, 18, 19, 44, 472109, tzinfo=utc)),
        ),
    ]
