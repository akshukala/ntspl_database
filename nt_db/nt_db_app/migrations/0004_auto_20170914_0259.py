# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nt_db_app', '0003_auto_20170914_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Junction_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hour', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('second', models.IntegerField()),
                ('day', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('phase_no', models.IntegerField()),
                ('status', models.CharField(max_length=10, choices=[(b'3', b'GREEN'), (b'4', b'AMBER')])),
                ('normal_time', models.IntegerField()),
                ('step_elased_time', models.IntegerField()),
                ('cycle_elased_time1', models.IntegerField()),
                ('cycle_elased_time2', models.IntegerField()),
                ('working_on', models.CharField(max_length=10, choices=[(b'1', b'OFF'), (b'2', b'BLINKER'), (b'3', b'SIGNAL')])),
                ('mode', models.CharField(max_length=10, choices=[(b'1', b'OFF'), (b'2', b'BLINKER'), (b'3', b'SIGNAL')])),
                ('total_cycle_time1', models.CharField(max_length=10, choices=[(b'02', b'AUTO'), (b'03', b'MANUAL')])),
                ('total_cycle_time2', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(related_name='junction_data_entered', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='junction',
            name='cycle_elased_time1',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='cycle_elased_time2',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='day',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='minute',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='month',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='normal_time',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='phase_no',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='second',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='status',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='step_elased_time',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='total_cycle_time1',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='total_cycle_time2',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='working_on',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='year',
        ),
        migrations.AddField(
            model_name='junction_data',
            name='junction',
            field=models.ForeignKey(to='nt_db_app.Junction'),
        ),
        migrations.AddField(
            model_name='junction_data',
            name='modified_by',
            field=models.ForeignKey(related_name='junction_data_modified', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
