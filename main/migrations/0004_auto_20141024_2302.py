# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20141024_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photograph',
            name='data',
            field=models.ImageField(upload_to='/images/'),
        ),
    ]
