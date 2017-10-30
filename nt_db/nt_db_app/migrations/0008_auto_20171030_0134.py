# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nt_db_app', '0007_auto_20170919_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junction_data',
            name='status',
            field=models.CharField(max_length=10, choices=[(b'02', b'AMBER'), (b'03', b'GREEN'), (b'04', b'RED')]),
        ),
    ]
