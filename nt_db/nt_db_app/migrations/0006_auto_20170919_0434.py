# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nt_db_app', '0005_auto_20170919_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junction_data',
            name='mode',
            field=models.CharField(max_length=10, choices=[(b'02', b'AUTO'), (b'03', b'MANUAL')]),
        ),
        migrations.AlterField(
            model_name='junction_data',
            name='total_cycle_time1',
            field=models.IntegerField(),
        ),
    ]
