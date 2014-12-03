# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20141025_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photograph',
            options={'get_latest_by': 'creation_date'},
        ),
        migrations.AddField(
            model_name='photograph',
            name='creation_date',
            field=models.DateTimeField(default=datetime.date(2014, 10, 25), auto_now_add=True),
            preserve_default=False,
        ),
    ]
