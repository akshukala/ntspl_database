# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=20)),
                ('created_by', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(max_length=255)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Junction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('junction_name', models.CharField(max_length=20)),
                ('hour', models.IntegerField(max_length=2)),
                ('minute', models.IntegerField(max_length=2)),
                ('second', models.IntegerField(max_length=2)),
                ('day', models.IntegerField(max_length=2)),
                ('month', models.IntegerField(max_length=2)),
                ('year', models.IntegerField(max_length=4)),
                ('phase_no', models.IntegerField(max_length=2)),
                ('status', models.CharField(max_length=10, choices=[(b'3', b'GREEN'), (b'4', b'AMBER')])),
                ('normal_time', models.IntegerField(max_length=2)),
                ('step_elased_time', models.IntegerField(max_length=2)),
                ('cycle_elased_time1', models.IntegerField(max_length=2)),
                ('cycle_elased_time2', models.IntegerField(max_length=2)),
                ('working_on', models.CharField(max_length=10, choices=[(b'1', b'OFF'), (b'2', b'BLINKER'), (b'3', b'SIGNAL')])),
                ('mode', models.CharField(max_length=10, choices=[(b'1', b'OFF'), (b'2', b'BLINKER'), (b'3', b'SIGNAL')])),
                ('total_cycle_time1', models.CharField(max_length=10, choices=[(b'02', b'AUTO'), (b'03', b'MANUAL')])),
                ('total_cycle_time2', models.IntegerField(max_length=2)),
                ('created_by', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(max_length=255)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('city', models.ForeignKey(to='nt_db_app.City')),
            ],
        ),
    ]
