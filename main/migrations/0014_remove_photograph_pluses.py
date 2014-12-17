# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_photograph_pluses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photograph',
            name='pluses',
        ),
    ]
