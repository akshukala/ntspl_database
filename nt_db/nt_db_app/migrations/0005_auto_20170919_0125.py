# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nt_db_app', '0004_auto_20170914_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='junction',
            name='road_name1',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction',
            name='road_name2',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction',
            name='road_name3',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction',
            name='road_name4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction',
            name='road_name5',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction',
            name='road_name6',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction',
            name='road_name7',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction',
            name='road_name8',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction_data',
            name='phase1',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction_data',
            name='phase2',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction_data',
            name='phase3',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction_data',
            name='phase4',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction_data',
            name='phase5',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction_data',
            name='phase6',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction_data',
            name='phase7',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='junction_data',
            name='phase8',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
