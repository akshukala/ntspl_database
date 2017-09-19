# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nt_db_app', '0006_auto_20170919_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='junction_data',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='junction_data',
            name='modified_by',
        ),
    ]
