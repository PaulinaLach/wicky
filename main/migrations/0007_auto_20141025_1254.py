# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20141025_1206'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
        migrations.RemoveField(
            model_name='photograph',
            name='user',
        ),
    ]
