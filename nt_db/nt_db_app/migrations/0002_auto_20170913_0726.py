# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nt_db_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junction',
            name='cycle_elased_time1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='cycle_elased_time2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='day',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='hour',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='minute',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='month',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='normal_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='phase_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='second',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='step_elased_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='total_cycle_time2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='junction',
            name='year',
            field=models.IntegerField(),
        ),
    ]
