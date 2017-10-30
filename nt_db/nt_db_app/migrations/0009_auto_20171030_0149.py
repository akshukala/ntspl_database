# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nt_db_app', '0008_auto_20171030_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junction_data',
            name='cycle_elased_time1',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='junction_data',
            name='cycle_elased_time2',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='junction_data',
            name='total_cycle_time1',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='junction_data',
            name='total_cycle_time2',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
