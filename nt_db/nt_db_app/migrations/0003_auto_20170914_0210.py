# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('nt_db_app', '0002_auto_20170913_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='created_by',
            field=models.ForeignKey(related_name='city_entered', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='modified_by',
            field=models.ForeignKey(related_name='city_modified', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='junction',
            name='created_by',
            field=models.ForeignKey(related_name='junction_entered', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='junction',
            name='modified_by',
            field=models.ForeignKey(related_name='junction_modified', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
