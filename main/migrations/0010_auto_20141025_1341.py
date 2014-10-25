# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20141025_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='user_account',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='photograph',
            old_name='user_account',
            new_name='user',
        ),
    ]
