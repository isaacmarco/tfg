# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TFG_APP', '0008_auto_20170218_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('completado', models.BooleanField(default=False)),
                ('dificultad', models.CharField(max_length=100, default='facil')),
                ('tipo_operaciones', models.CharField(max_length=100, default='sumas')),
                ('numero_sesiones', models.IntegerField(default=5)),
                ('numero_items_por_sesion', models.IntegerField(default=10)),
                ('tiempo_minimo_entre_sesiones', models.IntegerField(default=12)),
                ('sujeto', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Planes',
            },
        ),
    ]
